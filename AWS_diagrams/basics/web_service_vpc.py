# with backgound colour
from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import VPC
from diagrams.aws.general import InternetAlt1
graph_attr = {
    "fontsize": "80",
    "bgcolor": "white"
}
with Diagram("EC2", show=False, graph_attr=graph_attr, filename="webserver_vpc", direction="LR"):
    with Cluster("VPC"):
        web = EC2("web")
        web - [EC2("slave1"),
               EC2("slave2")]
    InternetAlt1("Internet") >> InternetAlt1("Internet") >> Cluster("VPC")
