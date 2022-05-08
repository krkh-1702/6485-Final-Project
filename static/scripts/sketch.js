let img;
let vid;
let theta = 0;

function setup() {
  createCanvas(800, 600, WEBGL);

//   img = loadImage('assets/cat.jpg');
  vid = createVideo(['static/assets/walk-z-line-seed0-24fps.mp4']);
  vid.elt.muted = true;
  vid.loop();
  vid.hide();
}

function draw() {
  background(10);
  noStroke();
  orbitControl(5,5,5);   
  translate(0, 0, 0);
  push();
//   rotateZ(theta * mouseX * 0.001);
//   rotateX(theta * mouseX * 0.001);
//   rotateY(theta * mouseX * 0.001);
  //pass image as texture
  texture(vid);
  sphere(100);
  pop();
  theta += 0.05;
}
