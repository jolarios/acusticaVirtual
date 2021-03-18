let audioContext;
let scene;
let audioElement;
let audioElementSource;
let source;
let audioReady = false;

//Variables for room dimension and source/listener location
var widthR, heightR, depthR, widthS, heightS, depthS, widthL, heightL, depthL;


function validateForm(){
	
	var i, auxUp, auxDown, text, flag;
	let inputs = ["widthR", "heightR", "depthR", "widthS",
	 "heightS", "depthS", "widthL", "heightL", "depthL"];

	for(i = 0; i < inputs.length; i++){
		var x = document.forms["myForm"][inputs[i]].value;
		
		if(i < 4){ auxUp = 25; auxDown = 0.5;}
		else{auxUp = 12.5; auxDown = -12.5}


		if (isNaN(x) || x < auxDown || x > auxUp) {
    	text = "Input not valid";
    	flag = false;
  	}
  	else {
    	text = "Input OK";
    	flag = true;
  	}

  	if(flag){
  		widthR = document.forms["myForm"]["widthR"].value;
			heightR = document.forms["myForm"]["heightR"].value;
			depthR = document.forms["myForm"]["depthR"].value;
			widthS = document.forms["myForm"]["widthS"].value;
			heightS = document.forms["myForm"]["heightS"].value;
			depthS = document.forms["myForm"]["depthS"].value;
			widthL = document.forms["myForm"]["widthL"].value;
			heightL = document.forms["myForm"]["heightL"].value;
			depthL = document.forms["myForm"]["depthL"].value;

			text = "Input saved in var";
  	}
  	else{text = "Input cannot be saved";}
	}
	return text;
}





