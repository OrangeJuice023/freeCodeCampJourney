document.addEventListener("DOMContentLoaded", function() {
  // Load the data
  fetch('https://raw.githubusercontent.com/freeCodeCamp/ProjectReferenceData/master/GDP-data.json')
    .then(response => response.json())
    .then(data => {
      // Data parsing
      const dataset = data.data;

      // Chart dimensions
      const margin = { top: 50, right: 100, bottom: 100, left: 100 };
      const width = 900 - margin.left - margin.right;
      const height = 500 - margin.top - margin.bottom;

      // Create the SVG container
      const svg = d3.select("#chart")
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      // X and Y scales
      const xScale = d3.scaleBand()
        .domain(dataset.map(d => new Date(d[0])))
        .range([0, width])
        .padding(0.1);

      const yScale = d3.scaleLinear()
        .domain([0, d3.max(dataset, d => d[1])])
        .range([height, 0]);

      // X and Y axes
      const xAxis = d3.axisBottom(xScale)
        .ticks(d3.timeYear.every(5)) // Display ticks every 5 years
        .tickFormat(d3.timeFormat("%Y")); // Format the year

      const yAxis = d3.axisLeft(yScale);

      // Append axes to the chart
      svg.append("g")
        .attr("id", "x-axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)
        .selectAll("text")
        .style("text-anchor", "end") // Align tick text at the end
        .attr("transform", "rotate(-45)"); // Rotate tick text for better readability

      svg.append("g")
        .attr("id", "y-axis")
        .call(yAxis);

      // Tooltip
      const tooltip = d3.select("#tooltip");

      // Create bars
      svg.selectAll(".bar")
        .data(dataset)
        .enter()
        .append("rect")
        .attr("class", "bar")
        .attr("data-date", d => d[0])
        .attr("data-gdp", d => d[1])
        .attr("x", d => xScale(new Date(d[0])))
        .attr("y", d => yScale(d[1]))
        .attr("width", xScale.bandwidth())
        .attr("height", d => height - yScale(d[1]))
        .on("mouseover", (event, d) => {
          tooltip
            .attr("data-date", d[0])
            .html(`${d[0]}<br>$${d[1]} Billion`)
            .style("left", event.pageX + 10 + "px")
            .style("top", event.pageY - 30 + "px")
            .classed("hidden", false);
        })
        .on("mouseout", () => tooltip.classed("hidden", true));
    })
    .catch(error => console.error('Error loading the data:', error));
});
