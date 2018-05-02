#include <CImg.h>
#include <iostream>
#include <map>
#include <vector>
#include <fstream>
using namespace std;
using namespace cimg_library;

class imagenes{
	public: 
		float desviacion;
		float minimo;
		float maximo;
		float promedio;
		float varianza;
		CImg<float> imagen;
		vector<float> caract;//vector que contiene las caracteristicas
		string nombre;//nombre del archivo
		vector<string> name_imagenes;
		map<string , vector<float> > imag_matriz;
		int tipo;
	public:
		imagenes(int t);
		void insertar(string name);
		void quad(int num);
		void caracteristica();
		float get_minimo();
		float get_maximo();
		float get_promedio();
		float get_varianza();
		float get_desviacion();
		void generar(string archivo,int num);
		void all_caracteristicas();
		void mostrar();
};
imagenes ::imagenes(int t){
	tipo=t;
	desviacion=minimo=maximo=promedio=0;
	nombre ="";
}
void imagenes:: insertar(string name){
	nombre=name;
	imagen.load(name.c_str());
}
void imagenes::quad(int num){
	imagen =(imagen.haar(false,num)).crop(0,0, imagen.width()/pow(2,num), imagen.height()/pow(2,num));
	//imagen.haar(false,num);
	//mostrar();
}
void imagenes::caracteristica(){
	minimo =get_minimo();
	maximo =get_maximo();
	promedio =get_maximo();
	desviacion =get_desviacion();
	caract.push_back(minimo);
	caract.push_back(maximo);
	caract.push_back(promedio);
	caract.push_back(desviacion);
	 
       
	for(int i=0;i<caract.size();i++)
		cout<<caract[i]<<"  ";
	imag_matriz.insert(make_pair(nombre,caract));
	caract.clear();
}
void imagenes::all_caracteristicas(){
	ofstream myfile;
	float mini = imagen(0,0);
   	float maxi = imagen(0,0);
	float prom = 0.0;
	for(int i=0; i<=imagen.width()-1;i++)
   		for(int j=0;j<=imagen.height()-1;j++){
   			prom += imagen(i,j);
        	if(imagen(i,j)<mini)
            	mini = imagen(i,j);
            if(imagen(i,j)>maxi)
            	maxi = imagen(i,j);
   		}
   	minimo =mini;
   	maximo =maxi;
   	promedio= prom*1.0/256;
   	float count=0.0;
	for(int i=0; i<=imagen.width()-1;i++)
   		for(int j=0;j<=imagen.height()-1;j++)
            count +=pow(imagen(i,j)-promedio,2);
    desviacion =sqrt(count/256);
    varianza=(count/256);
    caract.push_back(minimo);
    caract.push_back(maximo);
    caract.push_back(varianza);
    caract.push_back(desviacion);
	 myfile.open ("caract.txt",ios::app);
	for(int i=0;i<caract.size();i++)
		myfile << caract[i]<<",";
		//cout<<caract[i]<<"  ";
	//cout<<endl;
	if(tipo==1)
		myfile <<"1";
	else if(tipo==0)
		myfile <<"0";
	myfile<<endl;
	myfile.close();

	imag_matriz.insert(make_pair(nombre,caract));
	caract.clear();

}
float imagenes:: get_minimo(){
	 float mini = imagen(0,0);
   for(int i=0; i<=imagen.width()-1;i++)
   		for(int j=0;j<=imagen.height()-1;j++)
        	if(imagen(i,j)<mini)
            	mini = imagen(i,j);
    return mini;

}
float imagenes:: get_maximo(){
   float maxi = imagen(0,0);
   for(int i=0; i<=imagen.width()-1;i++)
   		for(int j=0;j<=imagen.height()-1;j++)
        	if(imagen(i,j)>maxi)
            	maxi = imagen(i,j);
    return maxi;

}
float imagenes:: get_promedio(){
	float prom = 0.0;
   for(int i=0; i<=imagen.width()-1;i++)
   		for(int j=0;j<=imagen.height()-1;j++)
            prom += imagen(i,j);
    return prom/256;

}
float imagenes:: get_desviacion(){
	float prom =get_promedio();
	float count=0.0;
	for(int i=0; i<=imagen.width()-1;i++)
   		for(int j=0;j<=imagen.height()-1;j++)
            count +=pow(imagen(i,j)-prom,2);
    return sqrt(count/256);
}
float imagenes:: get_varianza(){
	float prom =get_promedio();
	float count=0.0;
	for(int i=0; i<=imagen.width()-1;i++)
   		for(int j=0;j<=imagen.height()-1;j++)
            count +=pow(imagen(i,j)-prom,2);
    return (count/256);
}
void imagenes:: generar(string archivo,int num){
	ifstream file(archivo.c_str());
	char buffer[1000];
	while(!file.eof()){
		file.getline(buffer,1000);
		name_imagenes.push_back(buffer);
		//cout<<buffer<<endl;
	}
	file.close();

	for (int i = 0; i < name_imagenes.size()-1; ++i)
	{
		//cout<<i<<endl;
		insertar(name_imagenes[i]);
		quad(num);
		all_caracteristicas();
	}
	
}
void imagenes:: mostrar(){
	(imagen).display();
}
int main(){
	imagenes gatos(1);
	gatos.generar("gatos.txt",3);
	imagenes perros(0);
	perros.generar("perros.txt",3);
	//g++ haar.cpp -w -lpthread -lX11 -o main
}
