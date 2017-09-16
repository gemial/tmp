#include <iostream>
#include <iomanip>

int main(){

	uint32_t A[3] = {0x10203040, 0x50607080, 0x90A0B0C0}, *B;

	std::cout << std::hex << A << " " << A[0] << " " << A[1] << " " << A[2] << std::endl;
	B = A;
	std::cout << std::hex << B << " " << B[0] << " " << B[1] << " " << B[2] << std::endl;

	std::cout << "               " << std::hex  << *B << " ";
	B++;
	std::cout << std::hex  << *B << " ";
	B++;
	std::cout << std::hex  << *B << std:: endl;

	B = (uint32_t*)(uint64_t(A) + 1);
	std::cout << std::hex << B << " " << *B << " " << std::endl;

	uint8_t *C = (uint8_t*) A;

	for (int i = 0; i < 12; i++) std::cout <<uint16_t(C[i]) << " ";
	std::cout << std::endl;
}