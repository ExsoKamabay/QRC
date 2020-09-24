from qrc_window import *;
class QR_console(QR_KMY):
    def __init__(self):
        setattr(self,"setBanner",(choice([
            cs(text2art(decode("UVJD"),"smisome1"),"#00ffff"),
            cs(text2art(decode("UVJD"),"isometric3"),"#00ffff"),
            cs(text2art(decode("UVJD"),"isometric4"),"#00ffff"),
            cs(text2art(decode("UVJD"),"impossible"),"#00ffff"),
            cs(text2art(decode("UVJD"),"isometric1"),"#00ffff"),
            cs(text2art(decode("UVJD"),"isometric2"),"#00ffff"),
        ])));print("\t",getattr(self,"setBanner"));
        for opt in [
            (decor("barcode1"),text2art("1. QR-Normally ","awesome"),decor("barcode1")),
            (decor("barcode1"),text2art("2. QR-Bg - gif ","awesome"),decor("barcode1")),
            (decor("barcode1"),text2art("3. QR-Wifi-data","awesome"),decor("barcode1")),
            (decor("barcode1"),text2art("4. QR-geo -data","awesome"),decor("barcode1")),
            (decor("barcode1"),text2art("0.   Exit      ","awesome"),decor("barcode1"))]:
            print(cs(opt,"#00ffff"));
    def main(self):
        setattr(self,"modIn",(cs(decor("wave3")+" Nmbr : ","#9933ff")));
        setattr(self,"input",(int(input(getattr(self,"modIn")))));
        if getattr(self,"input") == 1:
            setattr(self,"modDt",(cs(decor("wave3")+" DATA : ","#9933ff")));
            setattr(self,"nmOut",(cs("name out > ","#9933ff")))
            setattr(self,"data",(input(getattr(self,"modDt"))));
            setattr(self,"modOut",(cs("\t\t  < set output >\nversion:num  scale:num  border:num  bg-color:chr  color:chr\n>  ","#9933ff")));
            setattr(self,"setOut",(input(getattr(self,"modOut"))).split());
            setattr(self,"output",(input(getattr(self,"nmOut"))));
            setattr(self,"data_dict",({
                "data":getattr(self,"data"),
                "version":getattr(self,"setOut")[0],
                "scale":getattr(self,"setOut")[1],
                "border":getattr(self,"setOut")[2],
                "bg-color":getattr(self,"setOut")[3],
                "color":getattr(self,"setOut")[4],
                "path out":getattr(self,"output")+".png",
            }));
            setattr(self,"set_value",(super().qr_std(
                value=getattr(self,"data"),bgColor=getattr(self,"setOut")[3],
                version=int(getattr(self,"setOut")[0]),color=getattr(self,"setOut")[4],
                scale=int(getattr(self,"setOut")[1]),border=int(getattr(self,"setOut")[2]),
                output=(getattr(self,"output")+".png")
            )));getattr(self,"set_value");system("clear");
            print(cs(dumps(getattr(self,"data_dict"),indent=1),"#9933ff"));
            QR_console().main();
        elif getattr(self,"input") == 2:
            setattr(self,"modDt",(cs(decor("wave3")+" DATA : ","#9933ff")));
            setattr(self,"nmOut",(cs("name out > ","#9933ff")))
            setattr(self,"data",(input(getattr(self,"modDt"))));
            setattr(self,"modOut",(cs("\t\t\t< set output >\nversion:num  scale:num  border:num  bg-color:chr  color:chr  bg-gif:chr\n%s "%(decor("title1")),"#9933ff")));
            setattr(self,"setOut",(input(getattr(self,"modOut"))).split());
            setattr(self,"output",(input(getattr(self,"nmOut"))));
            setattr(self,"data_dict",({
                "data":getattr(self,"data"),
                "version":getattr(self,"setOut")[0],
                "scale":getattr(self,"setOut")[1],
                "border":getattr(self,"setOut")[2],
                "bg-color":getattr(self,"setOut")[3],
                "bg-gif":getattr(self,"setOut")[5],
                "color":getattr(self,"setOut")[4],
                "path out":getattr(self,"output")+".gif",
            }));
            setattr(self,"set_value",(super().qr_gif(
                value=getattr(self,"data"),bgColor=getattr(self,"setOut")[3],
                version=int(getattr(self,"setOut")[0]),color=getattr(self,"setOut")[4],
                scale=int(getattr(self,"setOut")[1]),border=int(getattr(self,"setOut")[2]),
                bgGif=getattr(self,"setOut")[5],output=(getattr(self,"output"))
            )));getattr(self,"set_value");system("clear");
            print(cs(dumps(getattr(self,"data_dict"),indent=1),"#9933ff"));
            QR_console().main();
        elif getattr(self,"input") == 3:
            print(cs("\t< set data >\nssid -> password -> security","#9933ff"))
            setattr(self,"modDt",(cs(decor("wave3")+" DATA : ","#9933ff")));
            setattr(self,"nmOut",(cs("name out > ","#9933ff")))
            setattr(self,"data",(input(getattr(self,"modDt"))).split());
            setattr(self,"modOut",(cs("\t\t\t< set output >\nversion:num  scale:num  border:num  color:chr  bg-color:chr\n%s "%(decor("title1")),"#9933ff")));
            setattr(self,"setOut",(input(getattr(self,"modOut"))).split());
            setattr(self,"output",(input(getattr(self,"nmOut"))));
            setattr(self,"setVal",(dumps(super().qr_wisec(
                ssid=getattr(self,"data")[0],password=getattr(self,"data")[1],
                security=getattr(self,"data")[2],color=getattr(self,"setOut")[3],
                bgClr=getattr(self,"setOut")[4],version=int(getattr(self,"setOut")[0]),
                scale=int(getattr(self,"setOut")[1]),border=int(getattr(self,"setOut")[2]),
                output=getattr(self,"output")+".png"),indent=1)));system("clear");
            print(cs(getattr(self,"setVal"),"#9933ff"));QR_console().main();
        elif getattr(self,"input") == 4:
            print(cs("\t< set data >\nlatitude:float - longitude:float","#9933ff"))
            setattr(self,"modDt",(cs(decor("wave3")+" DATA : ","#9933ff")));
            setattr(self,"nmOut",(cs("name out > ","#9933ff")))
            setattr(self,"data",(input(getattr(self,"modDt"))).split());
            setattr(self,"modOut",(cs("\t\t\t< set output >\nversion:num  scale:num  border:num  color:chr  bg-color:chr\n%s "%(decor("title1")),"#9933ff")));
            setattr(self,"setOut",(input(getattr(self,"modOut"))).split());
            setattr(self,"output",(input(getattr(self,"nmOut"))));
            setattr(self,"setVal",(dumps(super().qr_location(latitude=float(getattr(self,"data")[0]),
            longitude=float(getattr(self,"data")[1]),color=getattr(self,"setOut")[3],
            bgClr=getattr(self,"setOut")[4],version=int(getattr(self,"setOut")[0]),
            scale=int(getattr(self,"setOut")[1]),border=int(getattr(self,"setOut")[2]),
            output=getattr(self,"output")+".png"),indent=1)));system("clear");
            print(cs(getattr(self,"setVal"),"#9933ff"));QR_console().main();
        elif getattr(self,"input") == 0:
            setattr(self,"chnel",("WW91dHViZSA6IGh0dHBzOi8vd3d3LnlvdXR1YmUuY29tL2NoYW5uZWwvVUNDa0ZQV2JRYXFvblBjNTF1VmVLdnln"));
            system("clear");print(cs(text2art(decode("YnllLWJ5ZQ"),"bear"),"#0000ff"));
            print(cs(decode(getattr(self,"chnel")),"#0000ff"));
        else:
            system("clear");print(cs(text2art(decode("RVJST1I"),"3d_diagonal"),"#ff3300"));
            print("\t",cs(decode("SW5jb3JyZWN0IGlucHV0LCBwbGVhc2UgdHJ5IGFnYWluIQ"),"#0000ff"));
if __name__=="__main__":
    QR_console().main()
