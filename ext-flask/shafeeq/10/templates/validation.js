function checkdata(){

	if(document.getElementById("A").value==""){
		alert("First number is missing");
		document.getElementById("A").focus();
		event.preventDefault();
	}
	else{
	if(document.getElementById("B").value==""){
		alert("Second number is missing");
		document.getElementById("B").focus();
		event.preventDefault();
	}
	}
}