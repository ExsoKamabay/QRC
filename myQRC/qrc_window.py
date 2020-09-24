from src import *
#js api
class QR_KMY:
    # QR Code Standard
    def qr_std(self,value=None,bgColor="cyan",version=1,
    color="black",scale=15,border=1,output="out.png"):
        dt = {#settings
            "val":value,
            "bgClr":bgColor,
            "vrsn":version,
            "color":color,
            "scale":scale,
            "border":border,
            "output":output};
        setattr(self,"value",(make(dt["val"],version=dt["vrsn"],error="h")));
        setattr(self,"setVal",(getattr(self,"value").to_pil(dark=dt["color"],
        light=dt["bgClr"],scale=dt["scale"],border=dt["border"])));
        getattr(self,"setVal").save(dt["output"]);return dt;
    # QR Code Gif background
    def qr_gif(self,value=None,bgColor="green",
    bgGif="%s"%(decode("c3JjL2JhY2tncm91bmQvYmcuZ2lm")),version=1,
    color="cyan",scale=15,border=1,output="out.gif"):
        dt = {#settings
            "val":value,
            "bgClr":bgColor,
            "bgGif":bgGif,
            "vrsn":version,
            "color":color,
            "scale":scale,
            "border":border,
            "output":output};
        setattr(self,"value",(make(dt["val"],version=dt["vrsn"],error="h")));
        setattr(self,"setVal",(getattr(self,"value").to_artistic(
        background=dt["bgGif"],target=dt["output"]+".gif",
        scale=dt["scale"],border=dt["border"],
        light=dt["color"],dark=dt["bgClr"])));return dt;
    #QR Wifi Secutity
    def qr_wisec(self,
    ssid=None,password=None,security=None,
    color="cyan",bgClr="black",version=5,
    scale=15,border=1,output="out.png"):
        dt = {#settings
            "ssid":ssid,
            "pass":password,
            "security":security,
            "output":output,
            "color":color,
            "bgClr":bgClr,
            "version":version,
            "scale":scale,
            "border":border}
        setattr(self,"network",(helpers.make_wifi_data(ssid=dt["ssid"],
        password=dt["pass"],security=dt["security"])));
        setattr(self,"setNet",(make(getattr(self,"network"),version=dt["version"])));
        setattr(self,"setSty",(getattr(self,"setNet").to_pil(dark=dt["color"],
        light=dt["bgClr"],scale=dt["scale"],border=dt["border"])));
        getattr(self,"setSty").save(dt["output"]);return dt;
    #QR Code Location
    def qr_location(self,
    latitude=None,longitude=None,output="out.png",
    color="cyan",bgClr="black",version=1,scale=15,border=1):
        dt = {#settings
            "latitude":latitude,
            "longitude":longitude,
            "output":output,
            "color":color,
            "bgClr":bgClr,
            "version":version,
            "scale":scale,
            "border":border};
        setattr(self,"location",(helpers.make_geo_data(dt["latitude"],dt["longitude"])));
        setattr(self,"setLocal",(make(getattr(self,"location"),error="h")));
        setattr(self,"setStyle",(getattr(self,"setLocal").to_pil(dark=dt["color"],
        light=dt["bgClr"],scale=dt["scale"],border=dt["border"])));
        getattr(self,"setStyle").save(dt["output"]);return dt;
    def window_qrGif(self,value,output):
        return self.qr_gif(value=value,output=output);
if __name__=="__main__":
    kamabay = QR_KMY();
    window = create_window(decode("UVItS0FNQUJBWQ"),html=html,js_api=kamabay,min_size=(900,900));
    start(loadCSS,window);


