/* Choropleth of visitors by country for /visitors/.
 *
 * Lives in its own file on purpose: the site's compress layout strips newlines
 * from page HTML, which turns any // comment in an inline <script> into a
 * comment that swallows the rest of the file. Assets are served untouched.
 *
 * Reads its data from the JSON handed over in #visitor-data, and the country
 * outlines from a vendored copy of world-atlas, so the page makes no
 * third-party request at view time.
 */
(function () {
  var dataEl = document.getElementById("visitor-data");
  var root = document.getElementById("visitor-map-root");
  if (!dataEl || !root || typeof d3 === "undefined" || typeof topojson === "undefined") return;

  var payload = JSON.parse(dataEl.textContent);
  var rows = payload.rows || [];
  var iso = payload.iso || {};
  var atlasUrl = payload.atlas;

  /* visitors keyed by ISO 3166-1 numeric, which world-atlas uses as feature id */
  var byNumeric = {}, nameByNumeric = {};
  rows.forEach(function (r) {
    var num = iso[r.code];
    if (!num) return;                      /* e.g. XK (Kosovo) has no numeric code */
    byNumeric[num] = (byNumeric[num] || 0) + r.visitors;
    nameByNumeric[num] = r.name;
  });

  /* Sequential encoding: one hue, light -> dark. Thresholds rather than a linear
     scale, because visitor counts are heavily skewed towards a few countries. */
  var BREAKS = [1, 2, 5, 20, 100, 500];
  var BIN_LABELS = ["1", "2–4", "5–19", "20–99", "100–499", "500+"];
  var ANTARCTICA = "010";                  /* no visitors, and it eats the frame */
  var W = 960, H = 430;

  function styles() {
    var cs = getComputedStyle(root);
    return {
      ramp: [1, 2, 3, 4, 5, 6].map(function (i) {
        return cs.getPropertyValue("--seq-" + i).trim();
      }),
      noData: cs.getPropertyValue("--no-data").trim(),
      sep: cs.getPropertyValue("--surface-1").trim(),
      ocean: cs.getPropertyValue("--ocean").trim()
    };
  }

  function binOf(v) {
    if (!v) return -1;
    var i = BREAKS.length - 1;
    while (i > 0 && v < BREAKS[i]) i--;
    return i;
  }

  var svg = d3.select("#visitor-map")
      .attr("viewBox", "0 0 " + W + " " + H)
      .attr("preserveAspectRatio", "xMidYMid meet");
  var tip = d3.select("#visitor-tooltip");

  d3.json(atlasUrl).then(function (world) {
    var countries = topojson.feature(world, world.objects.countries).features
        .filter(function (d) { return d.id !== ANTARCTICA; });
    /* Equal Earth is equal-area, so shaded areas stay comparable */
    var projection = d3.geoEqualEarth()
        .fitSize([W, H], { type: "FeatureCollection", features: countries });
    var path = d3.geoPath(projection);

    function paint() {
      var s = styles();
      svg.selectAll("*").remove();

      svg.append("rect").attr("width", W).attr("height", H).attr("fill", s.ocean);

      svg.append("g").selectAll("path")
        .data(countries)
        .join("path")
          .attr("d", path)
          /* hairline in the surface colour keeps adjacent fills from merging */
          .attr("stroke", s.sep)
          .attr("stroke-width", 0.6)
          .attr("fill", function (d) {
            var b = binOf(byNumeric[d.id]);
            return b < 0 ? s.noData : s.ramp[b];
          })
          .attr("tabindex", function (d) { return byNumeric[d.id] ? 0 : null; })
          .on("mousemove focus", function (event, d) {
            var v = byNumeric[d.id];
            if (!v) return;
            var name = nameByNumeric[d.id] || (d.properties && d.properties.name) || "";
            tip.attr("hidden", null)
               .html("<b>" + name + "</b><br>" + v + (v === 1 ? " visitor" : " visitors"));
            var wrap = document.querySelector(".viz-map-wrap").getBoundingClientRect();
            var x = (event.clientX || wrap.left + wrap.width / 2) - wrap.left;
            var y = (event.clientY || wrap.top + wrap.height / 2) - wrap.top;
            tip.style("left", Math.min(Math.max(x + 12, 4), wrap.width - 150) + "px")
               .style("top", Math.max(y - 44, 4) + "px");
          })
          .on("mouseleave blur", function () { tip.attr("hidden", true); });

      var legend = d3.select("#visitor-legend");
      legend.selectAll("*").remove();
      legend.append("span").attr("class", "viz-legend-title").text("Visitors");
      BIN_LABELS.forEach(function (label, i) {
        var item = legend.append("span").attr("class", "viz-legend-item");
        item.append("span").attr("class", "viz-swatch").style("background", s.ramp[i]);
        item.append("span").text(label);
      });
      var none = legend.append("span").attr("class", "viz-legend-item");
      none.append("span").attr("class", "viz-swatch").style("background", s.noData);
      none.append("span").text("none");
    }

    paint();
    if (window.matchMedia) {
      var mq = window.matchMedia("(prefers-color-scheme: dark)");
      if (mq.addEventListener) mq.addEventListener("change", paint);
      else if (mq.addListener) mq.addListener(paint);
    }
  }).catch(function () {
    d3.select("#visitor-map").attr("hidden", true);
    d3.select("#visitor-legend")
      .text("The map could not be loaded; the table below has the same data.");
  });
})();
