
/**
*This is the JS that contains some function to do some operation on the html file
*@author Edison Pan
*email pandigreat@bupt.edu.cn
**/

/*
This is a function that to show show content when you click navigate-slide
and the nav bar will be active
*/

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
	alert(cele)
	$(cele).show(1000)
	$(hele).show(1000)
}

