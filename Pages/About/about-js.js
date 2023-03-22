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
  
const faders = document.querySelectorAll('.fade-in');
const appearOptions= {
  threshold: 0,
  rootMargin: "0px 0px -250px 0px"
};
const appearOnScroll = new IntersectionObserver
(function(entries,appearOnScroll) {
entries.forEach(entry => {
  if(!entry.isIntersecting){
    return;
  } else{
    entry.target.classList.add('appear');
    appearOnScroll.unobserve(entry.target);
  }
});
}, appearOptions);

faders.forEach(fader => {
  appearOnScroll.observe(fader);
});