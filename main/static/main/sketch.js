//setup constants

let height = 700;
let width = 400;

let doDraw=false;

//speed var
let L_speed = 0;
let R_speed = 0;

const increment=20;

let last_check;

//propotion constants
const rect_corner = 5;

const spaceing = 0.025
const rect_height = (0.8 - spaceing * 10) / 11;
const rect_width = 0.4;
const border = 0;
const text_height = rect_height;
const text_width = 0.2;
const textMulti = 0.6;


function setup() {
  let div = select('#can');
  //console.log(div);
  //console.log(div.size());
  width=div.size().width;

  let canvas = createCanvas(width, height);
  canvas.parent('can')
  smooth();
  rectMode(CORNER);

  sendSpeedData(0,0);
  //getSpeedData();
  let temp = speedVal;
  L_speed=0;
  R_speed=0;

  last_check = Date.now();
  noLoop();
}

function draw() {
  // if(millis()-last_check>=1000){
  //   getSpeedData();
  //   temp = speedVal;
  //   L_speed=temp.leftSpeed;
  //   R_speed=temp.rightSpeed;
  //   last_check = millis();
  // }
  //console.log("123");

  clear();

  fill(200);
  strokeWeight(0);
  stroke(125);
  //textAlign(CENTER);

  for (let i = 0; i < 11; i++) {
    //81, 150, 68 - green 
    //201, 28, 28 - red

    let r, g, b;
    let temp;

    if (i != 5) {

      strokeWeight(0);

      if (i < 5) {
        temp = 5 - i;
      }
      else {
        temp = i - 5;
      }

      r = trans(temp, 1, 5, 81, 201);
      g = trans(temp, 1, 5, 150, 28);
      b = trans(temp, 1, 5, 68, 28)
    }
    else {
      //94, 153, 83 - base green
      temp = 0
      r = 94;
      g = 152;
      b = 83;
    }

    if ((L_speed / 20 >= temp && i <= 5 && L_speed >= 0) || (-1 * (L_speed / 20) >= temp && i >= 5 && L_speed <= 0)) {
      fill(color(r, g, b));
      //console.log(temp);
    }
    else {
      fill(200);
    }
    rect(border * width, border * height + i * rect_height * height + i * spaceing * height, rect_width * width, rect_height * height, rect_corner);

    if ((R_speed / 20 >= temp && i <= 5 && R_speed >= 0) || (-1 * (R_speed / 20) >= temp && i >= 5 && R_speed <= 0)) {
      fill(color(r, g, b));
      //console.log(temp);
    }
    else {
      fill(200);
    }
    rect(border * width + text_width * width + rect_width * width, border * height + i * rect_height * height + i * spaceing * height, rect_width * width, rect_height * height, rect_corner);
  }

  fill(0);
  strokeWeight(0);
  textAlign(CENTER, CENTER);
  textSize(height * (text_height - 0.02) * textMulti);
  //textFont("Big Caslon");


  for (let i = 0; i < 11; i++) {
    text(Math.floor(100 - i * 20) + '%', border * width + rect_width * width, border * height + i * rect_height * height + i * spaceing * height, text_width * width, text_height * height);
  }
  //noLoop();
}

const trans = (val, smin, smax, emin, emax) => {
  let ssize = smax - smin;
  let msize = emax - emin;

  val -= smin;
  val /= ssize;
  val *= msize;
  val += emin;

  return val;
}

const normalise = (val) =>{
  if(val>100){
    val=100;
  }
  if(val<-100){
    val=-100;
  }
  return val;
}

document.addEventListener('keydown', logKey);

function logKey(e) {
  if(e.code==='KeyI'){
    L_speed+=increment;
    L_speed=normalise(L_speed);
  }
  if(e.code==='KeyK'){
    L_speed-=increment;
    L_speed=normalise(L_speed);
  }
  if(e.code==='KeyP'){
    R_speed+=increment;
    R_speed=normalise(R_speed);
  }
  if(e.code==='Semicolon'){
    R_speed-=increment;
    R_speed=normalise(R_speed);
  }
  if(e.code==='KeyO'){
    R_speed+=increment;
    R_speed=normalise(R_speed);
    L_speed+=increment;
    L_speed=normalise(L_speed);
  }
  if(e.code==='KeyL'){
    R_speed-=increment;
    R_speed=normalise(R_speed);
    L_speed-=increment;
    L_speed=normalise(L_speed);
  }
  if(e.code==='Space'){
    R_speed=0;
    L_speed=0;
  }
  
  last_check = Date.now();
  sendSpeedData(L_speed,R_speed);
  redraw();

}



function windowResized(){
  let div = select('#can');
  //console.log(div);
  //console.log(div.size());
  width=div.size().width;
  resizeCanvas(width, height);
  redraw();
}


