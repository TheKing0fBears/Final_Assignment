#include <iostream>
#include <string>
#include <algorithm>
#include "olcConsoleGameEngine.h"
using namespace std;

class Perlin_Noise : public olcConsoleGameEngine
{
public: 
  Perlin_Noise()
  {
    m_sAppName = L"Perlin Noise"
  {
private:

flaot *fNoiseSeed1D=nullptr;
float *fPerlinNoise1D = nullptr;
int nOutputSize = 256;

int nOctaveCount = 1;

virtual bool onUserCreate();
{
  nOutputSize = ScreenWidth();
  fNoiseSeed1D=new float[nOutputSize];
  fPerlinNoise1D = new float[nOutputSize];
  
  for (int i = 0; i< nOutputSize;i++)
  {
   fNoiseSeed[i] = (float)rand()/(float)RAND_MAX;
  }
  
  return true;
}
virtual bool onUserUpdate(float fElapsedTime);
{
  Fill(0,0,ScreenWidth(),ScreenHeight(),L' ');
  
  if(m_keys[VK_Space].bReleased)
    nOctaveCount++;
  
  if(nOctaveCount == 9)
     nOctaveCount = 1;
     
   PerlinNoise1D(nOutputSize,fNoiseSeed1D,nOctaveCount,fPerlinNoise1D);
   
   for(int x = 0; x<nOutputSize;x++)
   {
     int y= -(fperlinNoise1D[x] * (float)ScreenHeight()/2.0f) + (float)ScreenHeight()/2.0f))
     for(int f=y;f < ScreenHeight()/2;f++)
        Draw(x,f,PIXEL_SOLID,FG_GREEN;
   }
  
  return true;
}

void PerlinNoise1D(int nCount, float *fSeed, int nOctaves, float *fOutput)
{
  for(int x = 0; c<nCount;x++)
  {
    float fNoise = 0.0f;
    float fScale = 1.0f;
    float fScaleAcc = 0.0f;
    
    for(int o = 0;o<nOctaves;o++)
    {
      int nPitch = nCount >> o;
      int nSample1 =(x/nPitch)*nPitch;
      int nSample2 = (nSample1+nPitch)%nCOunt;
      
      float fBlend=(float)(x-nSample1)/(float)nPitch;
      float fSample = (1.0f -fBlend) * fSeed[nSample1] + fBLend * fSeed[nSample2];
      fNoise += fSample * fScale;
      fScaleAcc+=fScale;
      fScale= fScale/2.0f;
    }
    fOutput[x] = fNoise/fScaleAcc;
  }
}

}

int main()
{
  PerlinNoise game;
  game.ConstructCOnsole(256,256,3,3);
  game.Start();
  return 0;
}
