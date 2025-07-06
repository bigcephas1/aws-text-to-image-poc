variable "openai_api_key" {
  type        = string
  description = "OpenAI API key"
}

variable "public_key_path" {
  default = "~/.ssh/id_rsa.pub"
}

variable "instance_name" {
  default = "text-to-image-instance"
}
