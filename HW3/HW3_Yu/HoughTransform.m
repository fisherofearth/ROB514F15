%% Hough Transform
close all
%Read an image into the MATLAB® workspace.
% I  = imread('circuit.tif');
I  = imread('Apple.jpg');
imshow(I);
I = rgb2gray(I);
% I = imrotate(I,33,'crop');
%Find the edges in the image using the edge function.
BW = edge(I,'canny',0.1);
figure
imshow(BW);

%Compute the Hough transform of the image using the hough function.
[H,theta,rho] = hough(BW,'RhoResolution',0.1,'ThetaResolution',0.1);

figure, imshow(imadjust(mat2gray(H)),[],'XData',theta,'YData',rho,...
        'InitialMagnification','fit');
xlabel('\theta (degrees)'), ylabel('\rho');
axis on, axis normal, hold on;

P = houghpeaks(H,5,'threshold',ceil(0.3*max(H(:))));
x = theta(P(:,2));
y = rho(P(:,1));
plot(x,y,'s','color','black');

%Find lines in the image using the houghlines function.
lines = houghlines(BW,theta,rho,P,'FillGap',5,'MinLength',7);
%Create a plot that superimposes the lines on the original image.
figure
imshow(I)
hold on
max_len = 0;
for k = 1:length(lines)
   xy = [lines(k).point1; lines(k).point2];
   plot(xy(:,1),xy(:,2),'LineWidth',2,'Color','green');
   % Plot beginnings and ends of lines
   plot(xy(1,1),xy(1,2),'x','LineWidth',2,'Color','yellow');
   plot(xy(2,1),xy(2,2),'x','LineWidth',2,'Color','red');
   % Determine the endpoints of the longest line segment
   len = norm(lines(k).point1 - lines(k).point2);
   if ( len > max_len)
      max_len = len;
      xy_long = xy;
   end
end

% highlight the longest line segment
plot(xy_long(:,1),xy_long(:,2),'LineWidth',2,'Color','red');