from diagrams import Cluster, Diagram, Edge
from diagrams.aws.compute import EC2
from diagrams.aws.network import VPC
from diagrams.aws.network import PublicSubnet
from diagrams.aws.network import PrivateSubnet
from diagrams.aws.network import NATGateway
from diagrams.aws.general import InternetAlt1
from diagrams.aws.general import InternetGateway
from diagrams.aws.network import RouteTable
from diagrams.aws.general import User

graph_attr = {
    "fontsize": "20",

}
node_attr = {
    "margin": "1000",
    "fontsize": "15",

}


with Diagram("VPC Public and Private Subnet", show=False, filename="VPC_public_Private", graph_attr=graph_attr, node_attr=node_attr):

    with Cluster("AWS"):
        with Cluster("VPC"):
            vpc = VPC('custom-vpc')
            out_inter = InternetAlt1('Internet')
            with Cluster("Public"):
                sub_public = PublicSubnet('Public Subnet')
                web = EC2("Bastion-Host")
                nat = NATGateway("NAT_Gateway")
                igw = InternetGateway('pubic-IGW')
                sub_public >> web
                out_inter >> igw >> sub_public >> nat
            with Cluster("Private"):
                sub_private = PrivateSubnet('Private Subnet')
                priv_ec2 = [EC2("app1"), EC2("app2")]

                out_inter >> igw >> sub_public >> nat >> priv_ec2
                sub_private >> priv_ec2
        web >> Edge(label='SSH') >> priv_ec2
        vpc >> sub_public
        vpc >> sub_private
    User('TOM') >> web
