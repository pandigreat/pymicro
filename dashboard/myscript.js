
/**
*This is the JS that contains some function to do some operation on the html file
*@author Edison Pan
*email pandigreat@bupt.edu.cn
**/

/*
This is a function that to show show content when you click navigate-slide
and the nav bar will be active
*/
/*
function showContent (obj){
	var element = document.getElementById(obj.id)
	name = obj.id.substr(0,3)
	num = 10
	for (var i = 1; i < num; i++){
		var c = name+i
		e = document.getElementById(c)
		isValue = $(e).hasClass("active");
		if (isValue == true){
			$(e).removeClass("active")
		}
	}
	$(element).addClass("active")
	var cname = "content" + obj.id.substr(3, 12)
	var hname = "head" + obj.id.substr(3, 12)
	for (var i = 1; i < num; i++){
		var cn = "content" + i
		var hn = "head" + i
		var ce = document.getElementById(cn)
		var he = document.getElementById(hn)
		$(ce).hide(1)
		$(he).hide(1)
	}
	var cele = document.getElementById(cname)
	var hele = document.getElementById(hname)
	$(cele).show(1000)
	$(hele).show(1000)
	DrawGraph(obj)
}
*/
function showContent (obj){
	var element = document.getElementById(obj.id)
	name = obj.id.substr(0,3)
	num = obj.id.substr(3, 12)
	 
	for (var i = 1; i < 10; i++){
		var c = name+i
		e = document.getElementById(c)
		isValue = $(e).hasClass("active");
		if (isValue == true){
			$(e).removeClass("active")
		}
	}
	$(element).addClass("active")
	/*Hidden All Contents and Heads*/
	for (var i = 1; i < 10; i++){
		var cn = "content" + i
		var hn = "head" + i
		var ce = document.getElementById(cn)
		var he = document.getElementById(hn)
		$(ce).hide(1)
		$(he).hide(1)
	}
	var cn = "content" + num
	var hn = "head" + num	
	var ce = document.getElementById(cn)
	var he = document.getElementById(hn)
	$(ce).show(1000)
	$(he).show(1000)
	if (num != 1){
		DrawGraph(obj)
	}

}




function DrawGraph(obj){
	var ele = document.getElementById(obj.id)
	var n = obj.id.substr(3,12)

	var content = '#' + 'content' + n
	var links2 = [
	  {source: "view", target: "serviceA", type: "suit"},
	  {source: "view", target: "serviceB", type: "suit"},
	  {source: "view", target: "serviceC", type: "suit"},
	  {source: "serviceA", target: "serviceA1", type: "suit"},
	  {source: "serviceA", target: "serviceA2", type: "suit"},
	  {source: "serviceA", target: "serviceA3", type: "suit"},
	  {source: "serviceB", target: "serviceB1", type: "suit"},
	  {source: "serviceB", target: "serviceB2", type: "suit"},
	  {source: "serviceB", target: "serviceB3", type: "suit"},
	  {source: "serviceC", target: "serviceC1", type: "suit"},
	  {source: "serviceC", target: "serviceC2", type: "suit"},
	  {source: "serviceC", target: "serviceC3", type: "suit"},
	  {source: "serviceC2", target: "serviceDB2", type: "licensing"},
	  {source: "serviceB3", target: "serviceDB3", type: "suit"},
	  {source: "serviceA1", target: "serviceDB1", type: "suit"},
			];
	var links3 = [
	  {source: "view", target: "serviceC2", type: "suit"},
	  {source: "serviceC2", target: "view", type: "suit"},
	  {source: "serviceC", target: "serviceDB2", type: "suit"},
	  {source: "serviceDB2", target: "serviceC", type: "suit"},
	  {source: "serviceC3", target: "serviceDB2", type: "suit"},
	  {source: "serviceDB2", target: "serviceC3", type: "suit"},
	  {source: "serviceC", target: "serviceC3", type: "suit"},
	  {source: "serviceC3", target: "serviceC", type: "suit"},
	  {source: "serviceB2", target: "serviceC1", type: "suit"},
	  {source: "serviceC1", target: "serviceB2", type: "suit"},
	  {source: "serviceA1", target: "serviceDB1", type: "suit"},
	  {source: "serviceDB3", target: "serviceDB1", type: "suit"},
	  {source: "serviceB1", target: "serviceB", type: "suit"},
	  {source: "serviceB", target: "serviceB2", type: "suit"},
	  {source: "serviceC1", target: "serviceB2", type: "suit"},
	  {source: "serviceB2", target: "serviceC1", type: "suit"},
	  {source: "serviceB", target: "serviceB1", type: "suit"}
	];
	var links4 = [
	  {source: "view", target: "serviceC2", type: "suit"},
	  {source: "serviceC2", target: "view", type: "suit"},
	  {source: "serviceC", target: "serviceDB2", type: "suit"},
	  {source: "serviceDB2", target: "serviceC", type: "suit"},
	  {source: "serviceC3", target: "serviceDB2", type: "suit"},
	  {source: "serviceDB2", target: "serviceC3", type: "suit"},
	  {source: "serviceC", target: "serviceC3", type: "suit"},
	  {source: "serviceC3", target: "serviceC", type: "suit"},
	  {source: "serviceB2", target: "serviceC1", type: "suit"},
	  {source: "serviceC1", target: "serviceB2", type: "suit"},
	  {source: "serviceA1", target: "serviceDB1", type: "suit"},
	  {source: "serviceDB3", target: "serviceDB1", type: "suit"},
	  {source: "serviceB1", target: "serviceB", type: "suit"},
	  {source: "serviceB", target: "serviceB2", type: "suit"},
	  {source: "serviceC1", target: "serviceB2", type: "suit"},
	  {source: "serviceB2", target: "serviceC1", type: "suit"},
	  {source: "serviceB", target: "serviceB1", type: "suit"},
	  {source: "view", target: "serviceA", type: "suit"},
	  {source: "view", target: "serviceB", type: "suit"},
	  {source: "view", target: "serviceC", type: "suit"}
	];
	var links = []
	switch(n){
		case "1":
			links = links1;
			break;
		case "2": 
			links = links2;
			break;
		case "3":
			links = links3;
			break;
		case "4":
			links = links4;
			break;
		case "5":
			links = links5;
			break;
		case "6":
			links = links6;
			break;
		default:
			alert('error: ' + n)
	}
	var nodes = {};

	// Compute the distinct nodes from the links.
	links.forEach(function(link) {
	  link.source = nodes[link.source] || (nodes[link.source] = {name: link.source});
	  link.target = nodes[link.target] || (nodes[link.target] = {name: link.target});
	});

	var width = 960, height = 500;

	var force = d3.layout.force()
		.nodes(d3.values(nodes))
		.links(links)
		.size([width, height])
		.linkDistance(60)
		.charge(-300)
		.on("tick", tick)
		.start();
	
	d3.selectAll("svg").style("display", "none")
	var svg = d3.select(content).append("svg")
		.attr("width", width)
		.attr("height", height);

	// Per-type markers, as they don't inherit styles.
	svg.append("defs").selectAll("marker")
		.data(["suit", "licensing", "resolved"])
	  .enter().append("marker")
		.attr("id", function(d) { return d; })
		.attr("viewBox", "0 -5 10 10")
		.attr("refX", 15)
		.attr("refY", -1.5)
		.attr("markerWidth", 6)
		.attr("markerHeight", 6)
		.attr("orient", "auto")
	  .append("path")
		.attr("d", "M0,-5L10,0L0,5");

	var path = svg.append("g").selectAll("path")
		.data(force.links())
	  .enter().append("path")
		.attr("class", function(d) { return "link " + d.type; })
		.attr("marker-end", function(d) { return "url(#" + d.type + ")"; });

	var circle = svg.append("g").selectAll("circle")
		.data(force.nodes())
	  .enter().append("circle")
		.attr("r", 6)
		.call(force.drag);

	var text = svg.append("g").selectAll("text")
		.data(force.nodes())
	  .enter().append("text")
		.attr("x", 8)
		.attr("y", ".31em")
		.text(function(d) { return d.name; });
	// Use elliptical arc path segments to doubly-encode directionality.
	function linkArc(d) {
	  var dx = d.target.x - d.source.x,
		  dy = d.target.y - d.source.y,
		  dr = Math.sqrt(dx * dx + dy * dy);
	  return "M" + d.source.x + "," + d.source.y + "A" + dr + "," + dr + " 0 0,1 " + d.target.x + "," + d.target.y;
	}

	function transform(d) {
	  return "translate(" + d.x + "," + d.y + ")";
	}

	function tick() {
	  path.attr("d", linkArc);
	  circle.attr("transform", transform);
	  text.attr("transform", transform);
	}

}


