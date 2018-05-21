    var ws;
    
    function invokeWebSocket() {

      // Connect to Web Socket
     //document.getElementsByTagName("img")[1].setAttribute("src", 'data:image/png;base64,'+ image); 

      ws = new WebSocket("ws://"+prompt("Enter IP address :")+":5678/");

      // Set event handlers.
      ws.onopen = function() {
        /*output("Connection Open");*/
        document.getElementById("log").innerHTML = "Connection Open";
      };
      
      ws.onmessage = function(e) {
        // e.data contains received string.
/*      var jsonObj = {
        dir:"dirTest",
        stdout:"stdTest",
        stderr:"errTest",
      };*/
/*      console.log(typeof e.data == 'object');
      console.log(typeof e.data == 'string');*/

      if (typeof e.data == 'object') {
        var image = new Blob([e.data], {type: 'image/png'});
       /* var image = e.data;*/
        var test =  window.URL.createObjectURL(image);
        /*console.log(test);*/
        document.getElementById("image_link").innerHTML = "Copy this and paste in your browser tab -> "+ test;
      }
      

      /*window.open(window.URL.createObjectURL(image));*/


/*
      var reader  = new FileReader();

      console.log(reader.readAsDataURL(image));
*/

/*      if (image == test) 
      {
        alert('Hello World');
        console.log(image);
      }
      */
     /* document.getElementsByTagName("img")[1].setAttribute("src",'data:image/png;base64,'+ window.URL.createObjectURL(image));*/

      /*alert(btoa(e.data));*/
      /*document.getElementById("image").innerHTML = btoa(e.data);*/

        if (typeof e.data == 'string') 
        {
          var jsonObj=JSON.parse(e.data);
          document.getElementById("currentWorkingDir").innerHTML = ("<i><u><b>" +jsonObj.dir+ "</b></i></u>");
          document.getElementById("stdout").innerHTML = jsonObj.stdout;
          document.getElementById("stderr").innerHTML = ("<u>" + jsonObj.stderr + "</u>");
          document.getElementById("modal-body").innerHTML = jsonObj.logData;
          document.getElementById("systemInfo").innerHTML = jsonObj.systemInfo;          
        }



     /* if (jsonObj.image_status == "true") {
        document.getElementById("img").attr("src",jsonObj.image_data);
        alert("tre");
        var dec = jsonObj.img;
        dec = 'data:image/png;base64,' + dec;
        $('#img').attr("src",dec);
        document.getElementById("img").innerHTML = dec;
      }*/
      /*output("$ " + e.data);*/
        /*output(jsonObj);*/
      };
      
      ws.onclose = function() {
        output("Connection Lost Please Reconnect");
      };

      ws.onerror = function(e) {
        output("Connection Lost Please Reconnect");
      };

    }
    
    function getLog() {
      ws.send('__getLog');
    };

    function getScreenshot() {
      ws.send('__screenshotEmail');
    };

    function shutdownNow() {
      ws.send('__shutdownSystem');
    }

    function onSubmit() {
      var input = document.getElementById("input");
      // You can send message to the Web Socket using ws.send.
      ws.send(input.value);
      output("Browser Prompt: " + input.value);
      input.value = "";
      input.focus();
    };
    
    function onCloseClick() {
      ws.close();
    };

    
    function output(str) {
/*    var log = document.getElementById("log");
      var escaped = str.replace(/&/, "&amp;").replace(/</, "&lt;").
      replace(/>/, "&gt;").replace(/"/, "&quot;"); // "
      log.innerHTML = escaped + "<br>" + log.innerHTML;*/
      document.getElementById("log").innerHTML = str;
/*    document.getElementById("currentWorkingDir").innerHTML = jsonObj.dir;
      document.getElementById("log").innerHTML = jsonObj.stdout;
      document.getElementById("log").innerHTML = ("<i><u>" + jsonObj.stderr + "<i><u>");*/
    };

/*
var ovar obj=JSON.parse(response);bj=JSON.parse(response);
$("#status").html("<b>"+obj.status+"</b>");
$("#report").html("<i><u>"+obj.report+"</u></i>")
*/