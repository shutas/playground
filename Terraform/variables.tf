# Variable Declaration and Assignment

variable "aws_region" {
  description = "AWS region to launch servers."
  default     = "us-east-2"
}

variable "ingress_ports" {
    type        = list(number)
    description = "List of ingress ports."
    default     = [10, 20, 30]
}

variable "egress_ports" {
    type        = list(number)
    description = "List of engress ports."
    default     = [40, 50, 60]
}