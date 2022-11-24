const $ = window.$;

$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
    data.results.forEach((film) => {
      $('ul#list_movies').append(`<li>${film.title}</li>`);
    });
  });
});
