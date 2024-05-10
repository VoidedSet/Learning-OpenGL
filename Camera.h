#ifndef CAMERA_H
#define CAMERA_H

#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <glm/gtx/rotate_vector.hpp>
#include <glm/gtx/vector_angle.hpp>

#include "ShaderClass.h"

class Camera {
	public:
		glm::vec3 Position, Orientation = glm::vec3(0.0f, 0.0f, -1.0f), Up = glm::vec3(0.0f, 0.7f, 0.0f);

		int width, height;
		float speed = 1.f, sensitivity = 100.0f;
		bool firstClick = true;

		Camera(int width, int height, glm::vec3 position);
		void Matrix(float FOVdeg, float nearPlane, float farPlane, Shader& shader, const char* uniform);
		void Inputs(GLFWwindow* window);
};
#endif // !CAMERA_H
