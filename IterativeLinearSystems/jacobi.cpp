#include <iostream>
#include "../Eigen/Dense"

double inf_norm(Eigen::Vector3d v)
{
  return v.lpNorm<Eigen::Infinity>();
}

void jacobi(Eigen::Matrix3d &C, Eigen::Vector3d &b, double tol)
{
  Eigen::Vector3d x0(0.,0.,0.);
  Eigen::Vector3d x;

  x = C*x0 + b;

  while(inf_norm(x-x0) > tol)
  {
    x0 = x;
    x = C*x0 + b;
  }
  
  std::cout << "Approximation to x vector: " << std::endl << x << std::endl;
}

int main()
{
  int i, j, n = 3;
  Eigen::Matrix3d A, C;
  Eigen::Vector3d b(1.,-1.,2.);

  // Solving Ax = b. Note that A must be a strictly diagonally dominant matrix:

  A <<  3., 1., 1.,
        0., 2., 1.,
        1., 2., 4.;
  
  for (i = 0; i < n; i++)
  {
    b(i) = b(i) / A(i,i);
    for (j = 0; j < n; j++)
    {
      if (i == j)
        C(i,j) = 0;
      else
        C(i,j) = -(A(i,j)/A(i,i)); 
    }
  }

  std::cout << "Coefficient matrix A:" << std::endl << A << std::endl;
  std::cout << "Vector b:" << std::endl << b << std::endl;
  std::cout << "Jacobi C matrix: " << std::endl << C << std::endl;

  jacobi(C, b, 0.01);
}
