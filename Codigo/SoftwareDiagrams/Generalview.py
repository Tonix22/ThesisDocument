from diagrams import Cluster, Diagram,Edge
from diagrams.aws.compute import ECS
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53
from diagrams.aws.ml import SagemakerModel
from diagrams.custom import Custom
from diagrams.digitalocean.storage import Volume

graphatt = {
"shape": "box",
"style": "rounded",
"labeljust": "l",
"pencolor": "#AEB6BE",
"fontname": "Sans-Serif",
"fontsize": "15",
}


with Diagram("NetworkDevelop", show=False):
    
    with Cluster("Networks",graph_attr=graphatt):
        Networks = [SagemakerModel("PhaseNet"),
                     SagemakerModel("PolarNet"),
                     SagemakerModel("GoldenModels")]
        
        Test     = Custom("Model Predict","./icons/icons8-lab-items-100.png")
        
    with Cluster("Recieved Class",graph_attr=graphatt):
        QAM = Custom("Tx QAM", "./icons/icons8-scatter-chart-100.png")
        Getter = Custom("__getitem__","./icons/braces.png")
        
        with Cluster("Channel Class",graph_attr=graphatt):
            db_primary = RDS("NLOS")
            db_primary - [RDS("LOS")]
          
        QAM >>Edge(color="blue")>> Getter
        db_primary >>Edge(color="blue")>> Getter
    
    with Cluster("Data Loader",graph_attr=graphatt):
        with Cluster("Data Set"):
            DataSet = [Volume("Train"),
                    Volume("Validation"),
                    Volume("Test/Predict")]
            
        with Cluster("Data Process"):
            Funcs   =  [Custom("Get Y","./icons/braces.png"),
                        Custom("LS/LMMSE/Zero","./icons/braces.png"),
                        Custom("BER_calc","./icons/braces.png"),
                        Custom("SNR_BER_TEST","./icons/braces.png")]
    
    with Cluster("Results"):
        CSV = Custom("CSV","./icons/icons8-export-csv-100.png")
        Plot = Custom("Plot", "./icons/icons8-plot-80.png")
        CSV-Edge(color="black")-Plot
        
    Getter>> Edge(color="black", style="bold")>>DataSet
    DataSet>>Edge(color="darkblue", style="bold")>>Funcs[0]
    Funcs[0] >>Edge(color="darkgreen", style="bold")>> Networks
    #SNR_BER_TEST to TEST
    Funcs[3] >> Edge(color="red", style="dashed")>> Test
    Test >> Edge(color="red", style="dashed")>>Funcs[2]
    Funcs[2] >>Edge(color="red", style="dashed") >> CSV
    #Golden Model to LMSE
    Funcs[1] <<Edge(color="black", style="dashed")<< Networks[2]
