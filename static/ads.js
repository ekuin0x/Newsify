(function(d,z,s){s.src='https://'+d+'/400/'+z;
try{
    (document.body||document.documentElement).appendChild(s)}catch(e){}
})('mutcheng.net',6308070,document.createElement('script'))
$(document).ready(()=>{
    $("#mainad a").attr("href", "//meenetiy.com/4/6308318") 
    $("#mainad a").attr("target", "_blank") 
    $("#mainad img").attr("src", "../static/media/mainad.png") 
    $("head").append("<meta name='monetag' content='814455d3c18c22b1b31ca903b35d4996'>")
})

let ad ;
setTimeout(() => {
    ad = 0
}, 5000);

$("body").click(()=>{
    if (ad == 0 ){  
        ad = 1
        alert(ad)
        window.open('//meenetiy.com/4/6308318', '_blank');
        setTimeout(()=>{
            ad = 0
        }, 8000)
    }
    
})