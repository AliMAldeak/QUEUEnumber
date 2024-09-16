setInterval(function () {
    var url = "http://127.0.0.1:8080/show";
    fetch(url).then(function(response) {
      return response.json();
    }).then(function(data) {
      document.querySelector("#temp").textContent = data.temp;
        document.querySelector("#humi").textContent = data.humi;
        document.querySelector("#stall").textContent = data.stall;
      if(data.img != ""){
        console.log(data);
        document.querySelector("#avatar").src = data.img;
        document.querySelector("#no").textContent = data.no;
      }else{
        document.querySelector("#avatar").src = "images/images.png";
        document.querySelector("#no").textContent =  "Waiting";
        document.querySelector("#no").setAttribute("style","width: 233.63px; height: 185.90px; left: 89.18px; top: 113.05px; position: absolute; text-align: center; color: #124559; font-size: 72px; font-family: Figma Hand; font-weight: 400; line-height: 124.80px; word-wrap: break-word");
        document.querySelector("#stall").textContent = 'no more customer';
        document.querySelector("#stall").setAttribute("style"," left: 50px; top: -130px; position: absolute; text-align: center; color: #EFF6E0; font-size: 48px; font-family: Figma Hand; font-weight: 400; line-height: 124.80px; white-space: nowrap;");
      }
    }).catch(function(err) {
      console.log('Fetch Error :-S', err);
      document.querySelector("#avatar").src = "images/images.png";
      document.querySelector("#no").textContent =  "Waiting";     
      document.querySelector("#no").setAttribute("style","width: 233.63px; height: 185.90px; left: 89.18px; top: 113.05px; position: absolute; text-align: center; color: #124559; font-size: 72px; font-family: Figma Hand; font-weight: 400; line-height: 124.80px; word-wrap: break-word")
    });
}, 1000);