void setup(){
 size(500, 500); 
}

void draw(){
 
  background(0,250,154); //cor
  
  circle(width/2, height/2, 350); //circ externo
  circle(width/2, height/2, 200); //circ interno
  
  float r_interno = 100;
  float r_externo = 175;
  float a = QUARTER_PI;
  float n = TWO_PI;
  float angle = HALF_PI;
  float j = 0;
 
  translate(width/2, height/2);
  
  beginShape();
  noFill();
  for(float i = 0; i < n; i += angle){
    
    if(j == PI/2){
      vertex(r_externo*cos((2*PI)/3), r_externo*sin((2*PI)/3));
    }
    else{
    float sx = r_externo*cos(j);
    float sy = r_externo*sin(j);
    
    vertex(sx, sy);
    }
     
    float x = r_interno*cos(a+i);
    float y = r_interno*sin(a+i);
    
    println(x, y);
    vertex(x, y);
    
    if(i == 0){
      vertex(r_externo*cos(PI/3), r_externo*sin(PI/3));
      vertex(-(r_interno*cos(angle*3)), -(r_interno*sin(angle*3)));
    }
    
    
     j += angle;
    
  }
  endShape(CLOSE);
  
}
