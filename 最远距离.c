#include <stdio.h>
#include <math.h>
int main(int argc, char const *argv[])
{
	double distance(double *p1,double *p2);
	int n;
	double m=0;
	double points[20][2]={0};
	scanf("%d",&n);
	for (int i=0;i<n;i++){
		double x,y;
		scanf("%lf %lf",&x,&y);
		points[i][0]=x;
		points[i][1]=y;
	}
	for (int i=0;i<n;i++){
		for (int j=i+1;j<n;j++){
			double d=distance(points[i],points[j]);
			if (d>m){
				m=d;
			}
		}
	}
	printf("%.4lf\n",m);
	return 0;
}
double distance(double *p1,double *p2){  //(x,y)
	double a=p1[0]-p2[0];
	double b=p1[1]-p2[1];
	double d=sqrt(a*a+b*b);
	return d;
}