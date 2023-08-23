document.addEventListener("DOMContentLoaded", function () {
  const width = 960;
  const height = 600;

  // Define color scale for the legend
  const colorScale = d3.scaleSequential(d3.interpolateBlues).domain([0, 100]);

  const svg = d3.select("body")
    .append("svg")
    .attr("width", width)
    .attr("height", height);

  // Load the data
  Promise.all([
    d3.json("https://cdn.freecodecamp.org/testable-projects-fcc/data/choropleth_map/counties.json"),
    d3.json("https://cdn.freecodecamp.org/testable-projects-fcc/data/choropleth_map/for_user_education.json")
  ]).then(([countyData, educationData]) => {
    // Create a map from data FIPS codes to education percentages
    const educationMap = new Map();
    educationData.forEach(item => educationMap.set(item.fips, item.bachelorsOrHigher));

    // Define the custom legend intervals
    const legendIntervals = [3, 12, 21, 30, 39, 48, 57, 66];

    // Draw counties
    svg.selectAll("path")
      .data(topojson.feature(countyData, countyData.objects.counties).features)
      .enter()
      .append("path")
      .attr("class", "county")
      .attr("data-fips", d => d.id)
      .attr("data-education", d => educationMap.get(d.id))
      .attr("fill", d => colorScale(educationMap.get(d.id)))
      .attr("stroke", "#fff") // Add a white stroke to highlight the county boundaries
      .attr("d", d3.geoPath())
      .on("mouseover", handleMouseOver)
      .on("mouseout", handleMouseOut);

    // Draw legend
    const legend = d3.select("#legend")
      .append("svg")
      .attr("width", 200)
      .attr("height", 80)
      .selectAll("g")
      .data(legendIntervals)
      .enter()
      .append("g")
      .attr("transform", (d, i) => `translate(${i * 30}, 0)`); // Add space between legend items

    legend.append("rect")
      .attr("class", "legend-item")
      .attr("y", 10)
      .attr("width", 25)
      .attr("height", 20)
      .attr("fill", d => colorScale(d));

    legend.append("text")
      .attr("class", "legend-label")
      .attr("x", 10)
      .attr("y", 35)
      .text(d => `${d}%`);
      
    // Handle tooltip
    function handleMouseOver(event, d) {
      const tooltip = d3.select("#tooltip");
      tooltip.style("opacity", 1);
      tooltip.html(`County: ${d.properties.name}, ${d.properties.state}<br>Educational attainment: ${educationMap.get(d.id)}%`)
        .attr("data-education", educationMap.get(d.id))
        .style("left", (event.pageX + 10) + "px")
        .style("top", (event.pageY + 10) + "px");
    }

    function handleMouseOut() {
      const tooltip = d3.select("#tooltip");
      tooltip.style("opacity", 0);
    }
  });
});
