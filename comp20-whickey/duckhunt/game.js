// Your work goes here...

function draw()
{
	var can = document.getElementById('game');
	var ctx = can.getContext('2d');


	//fill backgorung of canvas with "skyblue"
	ctx.fillStyle = "#87CEEB";
	ctx.fillRect(0, 0, can.width, can.height);

	//draw on the road
	ctx.fillStyle = "C96A1B";
	ctx.fillRect(0, 500, can.width, can.height);

	//plant tree
	ctx.drawImage(document.getElementById("sprites"), 0, 273, 105, 399 - 267, 0, 0, 300, 500);

	//draw grass/bushes
	ctx.drawImage(document.getElementById("sprites"), 65, 715, 899, 899-715, 0, 330, can.width + 65, 250);

	//draw dog
	ctx.drawImage(document.getElementById("sprites"), 125, 0, 180-125, 45, 300, can.height - 210, (3 *(180-125)), (3 * 45));

	//draw duck 1
	ctx.drawImage(document.getElementById("sprites"),130, 120, 165-130, 145-120, 200, 10,(3*(165-130)), (3*(145-120)));

	//draw duck 2
	ctx.drawImage(document.getElementById("sprites"),260, 155, 295-260, 190-155, 175, 300,(3*(295-260)), (3*(190-155)));

	//draw duck 3
	ctx.drawImage(document.getElementById("sprites"),80, 195, 113-80, 229-195, 400, 300, (3*(33)), (3*(34)));

	//draw duck 4
	ctx.drawImage(document.getElementById("sprites"), 80, 115, 115-80, 148-115, 450, 20,(3*( 115-80 )), (3*( 148-115 )));

	//draw duck 5
	ctx.drawImage(document.getElementById("sprites"), 210, 155, 240-210 , 190-155 , 650, 150,(3*( 240-210 )), (3*( 190-155 )));




}
