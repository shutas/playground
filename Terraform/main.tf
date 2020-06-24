# AWS Provider
provider "aws" {
  region = var.aws_region
}


# Application Load Balancer


# Security Group
resource "aws_security_group" "allow_tls" {
  name        = "allow_tls"
  description = "Allow TLS inbound traffic"
  #vpc_id      = "${aws_vpc.main.id}"

  dynamic "ingress" {
      for_each = var.ingress_ports
      content {
        from_port   = ingress.value
        to_port     = ingress.value
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
      }
  }

  dynamic "egress" {
    for_each = var.egress_ports
    iterator = port
      content {
        from_port   = port.value
        to_port     = port.value
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
      }
  }

  tags = {
    Name = "allow_tls"
  }

}


# Web Application Firewall
/*
module "waf-owasp-top-10-rules" {
  source  = "traveloka/waf-owasp-top-10-rules/aws"
  version = "0.2.0"
  # insert the 5 required variables here
  product_domain                 = "test_product_domain"
  service_name                   = "test_service_name"
  environment                    = "test_environment"
  description                    = "OWASP Top 10 Rules"
  target_scope                   = "global"
}
*/