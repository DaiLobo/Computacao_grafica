void setup(){
 size(500, 500); 
}

void draw(){
 
  background(26, 0, 0); //cor do fundo
  
/*  //Círculo
  //circle(width/2, height/2, 350);
  
  //Pentagono Externo
  noFill();
  float angulo = TWO_PI/5;
  int r = 175;
  translate(width/2, height/2);
  beginShape();
  for(float i=0.75; i<5; i++)
  {
    float x = r*cos(i*angulo);
    float y = r*sin(i*angulo);
    vertex(x,y);
  }
  endShape(CLOSE);
 
  
  //Pentagono Interno
  noFill();
  float a = -(TWO_PI/5);
  int rzinho = 70;
 // rotate(PI);
  beginShape();
  for(float i=0.75; i<5; i++)
  {
    float x = rzinho*cos(i*a);
    float y = rzinho*sin(i*a);
    vertex(x,y);
  }
  endShape(CLOSE);*/
  
  //Estrela
  fill(253, 193, 68);
  float angulo = TWO_PI/5;
  float angulo2 = -(TWO_PI/5);
  int r = round(map(mouseY, 0, width, 87.5, 175));
  int rzinho = 70;
  float j = 0;
  translate(width/2, height/2);
  
  beginShape();
  
  for(float i = 0.75; i < 5; i++)
  {
    float x = r*cos(i*angulo);
    float y = r*sin(i*angulo);
    vertex(x,y);
    
    if(i < 4){
      float x1 = rzinho*cos((i+3-j) * angulo2);
      float y1 = rzinho*sin((i+3-j) * angulo2);
      vertex(x1, y1);
      
      j = j+2;
    }
    else{
      float x1 = rzinho*cos(i * angulo2);
      float y1 = rzinho*sin(i * angulo2);
      vertex(x1, y1);
    }
    
  }
  endShape(CLOSE);
 
}
