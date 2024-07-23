#include <iostream>
using namespace std;

void Jug1 (int mat[5][3],int c[3]){
	int i,j;//Declaramos variables internas del procedimiento
	for (i=0;i<=2;i++){//Le pedimos al jugador 1 que vaya completando una bomba por columna
		do{
			cout<<".:|||||Ingrese la fila de la bomba para la columna "<<i+1<<"|||||:."<<endl;
			cin>>j;
			mat[j][i]=1;
		}
		while (j>=5 || j<0);//verificamos que la bomba este dentro de los parametros
		do{
			cout<<".:|||||Ingrese el color del cable que desactive la bomba|||||:."<<endl;//Pedimos que coloque el color del cable
			cout<<"1 Para rojo, 2 para verde y 3 para azul"<<endl;
			cin>>c[i];//almacenamos el valor del cable en un vector
		}
		while (c[i]!=1 && c[i]!=2 && c[i]!=3);//verificamos que sean validos los datos obtenidos
	}
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;//Colocamos muchos saltos de linea para que al momento de iniciar el siguiente procedimiento este la pantalla limpia
}
	
void Jug2 (int mat[5][3], int c[3],int est){
	int i,j,cable,intento,punt;//Declaramos variables internas
	intento=0;
	punt=50;//El jugador empieza con la puntuación maxima, si se equivoca se le iran descontando puntos
	j=0;//Inicialisamos los contadores y variables
	cout<<".:|||||Ahora es el turno del desactivador de bombas|||||:."<<endl;
		do{
			cout<<""<<endl;
			cout<<""<<endl;
			cout<<""<<endl;//Colocamos saltos de linea para diferenciar título de instrucciones de juego
			do{
				cout<<"¿En que fila de la columna "<<j+1<<" cree que se encuentra la bomba?"<<endl;
				cin>>i;
			}while(i>=5 || i<0);//Verificamos que los datos sean admisibles
			if(mat[i][j]==1){//Esto solo se iniciara si el jugador adivina la posicion de la bomba
				do{
					cout<<"Bien ahi encontramos una bomba, tenemos 3 cables el primero es rojo, el segundo verde y el tercero azul, cual cortamos ??"<<endl;
					cin>>cable;
				}while(cable!=1 && cable!=2 && cable!=3);//Verificamos que el dato elegido este dentro de los parametros esperados
				if(cable==c[j]){//Si adivina la posición se desactivara la bomba y se pasara a la proxima columna de la matriz y al proximo valor del vector cable
					cout<<""<<endl;
					cout<<""<<endl;
					cout<<""<<endl;
					cout<<"¡¡Que suerte loco, le pegaste, desarmamos la bomba, sos un geino papá!!"<<endl;
					j+=1;
					cout<<""<<endl;
					cout<<""<<endl;
					cout<<""<<endl;
					cout<<".:|||||Actualmente eres un desactivador de bombas de nivel: "<<punt<<"|||||:."<<endl;//En caso de que encuentre la bomba los puntos se mantienen
				}else{//Si falla al elegir el color de la bomba, igualamos los intentos a un valor que sobrepase el limite, por lo que terminara automaticamente el juego
					cout<<""<<endl;
					cout<<""<<endl;
					cout<<""<<endl;
					cout<<"¡¡Le erraste, vamos a morir!!"<<endl;
					intento=6;
					cout<<""<<endl;
					cout<<""<<endl;
					cout<<""<<endl;
					cout<<".:|||||Nos vemos obligados a bajarte tu nivel de desactivador a 0, no fuiste capaz de salvarnos|||||:."<<endl;
				}
			}else{//Esto sucedera en caso de que el jugador falle en su intento de encontrar la bomba
				if (intento!=5){//Mientras los intentos sean menores a 5 se mostrara ese mensaje y sumamos uno a su contador
					cout<<"No habia ningun bomba ahi compañero, tienes que afinar la punteria, nos queda otra oportunidad"<<endl;
					intento+=1;
					punt-=intento*5;//El contador es ir descontado niveles de manera progresiva, ya que mientras mas veces se equivoque, mas se le desonctara
				}else{//Si los intentos ya sobrepasan el limite se mostrara este mensaje y finalizamos el programa
					cout<<""<<endl;
					cout<<""<<endl;
					cout<<""<<endl;
					cout<<"¡¡Loco no hay mas chances, abandonamos la mision!!"<<endl;
					intento+=1;
					cout<<""<<endl;
					cout<<""<<endl;
					cout<<""<<endl;
					cout<<".:|||||No pudiste encontrar todas las bombas para desactivarlas, nos vemos obligadas a bajar tu nivel de desactivador a 0|||||:."<<endl;
				}
			}
		}while (intento<6 && j<=2);//Esta es la parte que indicara si se repite la ccion de jugar o no
		//va midiendo que los intentos no sobrepasen el limite, o que en caso se que se encuentren las bombas, que una vez llegadas las 3 
		//columnas se finalice el programa
}
int main(int argc, char *argv[]) {
	int mat[5][3];int c[3],est;
	int i,j;//Declaración de variables
	est=0;
	cout<<".:|||||Bienvenido a Bomb Disassembler|||||:."<<endl;//Presentamos las reglas del juego
	cout<<"Reglas:"<<endl;
	cout<<"1)Hay una bomba por columna"<<endl;
	cout<<"2)El jugador 1 Debera colocar 3 bombas, e indicar el color del cable que se debera cortar para desarmar dicha bomba"<<endl;
	cout<<"3)Para descativar una bomba el Jugador 2 debera acertar en la posición de esta y cortar el cable correcto"<<endl;
	cout<<"4)El juego terminara cuadno el jugador 2 desactive todas las bombas o cuando al encontrar una corte el cable incorrecto"<<endl;
	cout<<"5)El jugador 2 posee cinco intentos en total para encontrar la bomba"<<endl;
	cout<<"6)El jugador 2 iniciara la partida siendo un nivel 50 desactivador de bombas, en caso de que cometa errores se irán descontando puntos seguún el error cometido"<<endl;
	cout<<"7)Divertirse y que gane el mejor!!!"<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;
	cout<<""<<endl;//colocamos saltos de linea para que se vea mas limpia y ordenada la pantalla
	
	//Igualamos todos los valores de la matriz a 0
	for (i=0;i<=4;i++){
		for (j=0;j<=2;j++){
			mat[i][j]=0;
		}}
	//Llamamos al procedimiento para inciar las acciones del jugador 1
	Jug1(mat,c);
	//Llamamos el procedimiento del jugador 2
	Jug2(mat,c,est);
	
	//Comentario adicional: En el procedimiento el jugador 2 decidimos colocar 3 saltos de linea entre los mensajes de resultado para que estos se diferencien de una manera optima
	
	
	return 0;
}

