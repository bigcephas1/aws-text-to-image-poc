variable "public_key" {
  description = "SSH public key content"
  type        = string
}

variable "openai_api_key" {
  description = "OpenAI API key for the container"
  type        = string
}

variable "instance_name" {
  description = "Name tag for the EC2 instance"
  type        = string
  default     = "text-to-image-app"
}
