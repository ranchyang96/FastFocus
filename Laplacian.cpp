#include <highgui/highgui.hpp>
#include <imgproc/imgproc.hpp>
 
using namespace std;
using namespace cv;
 
int main()
{
	Mat imageSource = imread("1.jpg");
	Mat imageGrey;
 
	cvtColor(imageSource, imageGrey, CV_RGB2GRAY);
	Mat imageSobel;
 
	Laplacian(imageGrey, imageSobel, CV_16U);
	//Sobel(imageGrey, imageSobel, CV_16U, 1, 1);
 
	//图像的平均灰度
	double meanValue = 0.0;
	meanValue = mean(imageSobel)[0];
 
	//double to string
	stringstream meanValueStream;
	string meanValueString;
	meanValueStream << meanValue;
	meanValueStream >> meanValueString;
	meanValueString = "Articulation(Laplacian Method): " + meanValueString;
	putText(imageSource, meanValueString, Point(20, 50), CV_FONT_HERSHEY_COMPLEX, 0.8, Scalar(255, 255, 25), 2);
	imshow("Articulation", imageSource);
	waitKey();
}
