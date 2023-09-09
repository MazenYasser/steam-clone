function openPassword() {
    displayState = document.getElementById("passwordInput").style.display
    if (displayState === "none"){
    $(document.getElementById("passwordInput")).removeClass("fade-out");
    $(document.getElementById("passwordInput")).addClass("fade-in");
    document.getElementById("passwordInput").style.display = "block";
    document.getElementById("passwordInput").style.marginTop = "20px";
    }

    else if (displayState === "block"){
    $(document.getElementById("passwordInput")).removeClass("fade-in");
    $(document.getElementById("passwordInput")).addClass("fade-out");
    document.getElementById("passwordInput").style.display = "none";
    document.getElementById("passwordInput").style.marginTop = "0px";
    }

  }

  function openEmail() {
    displayState = document.getElementById("emailInput").style.display
    if (displayState === "none"){
    $(document.getElementById("emailInput")).removeClass("fade-out");
    $(document.getElementById("emailInput")).addClass("fade-in");
    document.getElementById("emailInput").style.display = "block";
    document.getElementById("emailInput").style.marginTop = "20px";
    }

    else if (displayState === "block"){
    $(document.getElementById("emailInput")).removeClass("fade-in");
    $(document.getElementById("emailInput")).addClass("fade-out");
    document.getElementById("emailInput").style.display = "none";
    document.getElementById("emailInput").style.marginTop = "0px";
    }
  }



function openInput(field){
    var target = event.target
    displayState = document.getElementById(target.id).style.display
    if (displayState === "none"){
    $(document.getElementById(target.id)).removeClass("fade-out");
    $(document.getElementById(target.id)).addClass("fade-in");
    document.getElementById(target.id).style.display = "block";
    document.getElementById(target.id).style.marginTop = "20px";
    }

    else if (displayState === "block"){
    $(document.getElementById(field)).removeClass("fade-in");
    $(document.getElementById(field)).addClass("fade-out");
    document.getElementById(field).style.display = "none";
    document.getElementById(field).style.marginTop = "0px";
    }
}