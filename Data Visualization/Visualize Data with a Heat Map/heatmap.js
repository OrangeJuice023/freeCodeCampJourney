const url =
  "https://raw.githubusercontent.com/freeCodeCamp/ProjectReferenceData/master/global-temperature.json";

const width = 1200;
const height = 600;
const padding = 60;
const legendWidth = 300;
const legendHeight = 20;

// Create SVG container
const svg = d3.select("#heatmap").attr("width", width).attr("height", height);

// Create tooltip
const tooltip = d3.select("#tooltip");

// Fetch data from the provided URL
d3.json(url).then((data) => {
  const baseTemperature = data.baseTemperature;
  const monthlyData = data.monthlyVariance;

  // Convert months to full month names
  const monthNames = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
  ];

  // Find the minimum and maximum years
  const minYear = d3.min(monthlyData, (d) => d.year);
  const maxYear = d3.max(monthlyData, (d) => d.year);

  // Create x and y scales
  const xScale = d3.scaleLinear().domain([minYear, maxYear]).range([padding, width - padding]);
  const yScale = d3.scaleBand().domain(monthNames).range([height - padding, padding]);

  // Fixed scale for the legend
  const legendMinTemp = 2.8;
  const legendMaxTemp = 12.8;

  const legendScale = d3
    .scaleLinear()
    .domain([legendMinTemp, legendMaxTemp])
    .range([0, legendWidth]);

  // Create color scale
  const minTemp = baseTemperature + d3.min(monthlyData, (d) => d.variance);
  const maxTemp = baseTemperature + d3.max(monthlyData, (d) => d.variance);
  const colorScale = d3.scaleSequential(d3.interpolateRdYlBu).domain([maxTemp, minTemp]);

  // Create x and y axes
  const xAxis = d3.axisBottom(xScale).tickFormat(d3.format("d"));
  const yAxis = d3.axisLeft(yScale).tickFormat((d, i) => monthNames[i]);

  // Append x and y axes
  svg.append("g")
    .attr("id", "x-axis")
    .attr("transform", `translate(0, ${height - padding})`)
    .call(xAxis);

  svg.append("g")
    .attr("id", "y-axis")
    .attr("transform", `translate(${padding}, 0)`)
    .call(yAxis);

  // Create cells representing the data
  svg.selectAll(".cell")
    .data(monthlyData)
    .enter()
    .append("rect")
    .attr("class", "cell")
    .attr("x", (d) => xScale(d.year))
    .attr("y", (d) => yScale(monthNames[d.month - 1]))
    .attr("width", (width - 2 * padding) / (maxYear - minYear + 1))
    .attr("height", yScale.bandwidth())
    .attr("data-month", (d) => d.month - 1)
    .attr("data-year", (d) => d.year)
    .attr("data-temp", (d) => baseTemperature + d.variance)
    .style("fill", (d) => colorScale(baseTemperature + d.variance))
    .on("mouseover", (event, d) => {
      tooltip.transition().duration(200).style("opacity", 0.9);
      tooltip
        .html(
          `${monthNames[d.month - 1]} ${d.year}<br />${(baseTemperature + d.variance).toFixed(2)}°C<br />${d.variance.toFixed(2)}°C`
        )
        .attr("data-year", d.year)
        .style("left", event.pageX + 10 + "px")
        .style("top", event.pageY - 30 + "px");
    })
    .on("mouseout", () => {
      tooltip.transition().duration(200).style("opacity", 0);
    });

  // Create the legend
  const legend = svg
    .append("g")
    .attr("id", "legend")
    .attr("transform", `translate(${width - padding - legendWidth}, ${height - padding + 20})`);

  const legendAxis = d3.axisBottom(legendScale).ticks(5);

  legend.append("g").call(legendAxis);

  legend
    .selectAll(".legend-rect")
    .data(d3.range(legendMinTemp, legendMaxTemp, (legendMaxTemp - legendMinTemp) / 40))
    .enter()
    .append("rect")
    .attr("class", "legend-rect")
    .attr("x", (d) => legendScale(d))
    .attr("width", legendWidth / 40)
    .attr("height", legendHeight)
    .style("fill", (d) => colorScale(d));
});
