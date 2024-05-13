#ifndef CAMERA_H
#define CAMERA_H

#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>
#include <glm/gtx/rotate_vector.hpp>
#include <glm/gtx/vector_angle.hpp>
#include <glm/vec3.hpp>

#include <fstream>
#include <sstream>
#include <string>

#include "ShaderClass.h"

class Camera {
	public:
		glm::vec3 Position, Orientation = glm::vec3(0.0f, 0.0f, -1.0f), Up = glm::vec3(0.0f, 1.0f, 0.0f);
		glm::mat4 cameraMatrix = glm::mat4(1.0f);

		int width, height;
		float speed = 0.01f, sensitivity = 100.0f;
		bool firstClick = true;

		Camera(int width, int height, glm::vec3 position);
		void updateMatrix(float FOVdeg, float nearPlane, float farPlane);
		void Matrix(Shader& shader, const char* uniform);
		void Inputs(GLFWwindow* window);
		void processInput();
};
#endif // !CAMERA_H
