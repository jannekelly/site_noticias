 Vue.component('post', {
    props:{
      titulo: String,
      texto: String,
      imagem: String
    },
    template:"#noticia",  
    delimiters : ['[[', ']]']  

  }); 


  let app=new Vue({
    el:"#noticias",
    delimiters : ['[[', ']]'] ,
    data:{
      
    }
  });


 
