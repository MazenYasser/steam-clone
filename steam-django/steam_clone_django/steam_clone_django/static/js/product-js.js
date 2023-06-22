function openNav() {
    document.getElementById("myNav").style.width = "50%";
    var elements = document.getElementsByClassName("bg");
    for(var i=0; i<elements.length; i++) { 
    elements[i].style.opacity='20%';
    }

  }
  
  function closeNav() {
    document.getElementById("myNav").style.width = "0%";
    var elements = document.getElementsByClassName("bg");
    for(var i=0; i<elements.length; i++) { 
    elements[i].style.opacity='100%';
    }
  }
  