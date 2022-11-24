const $ = window.$;

$(document).ready(function () {
  $.get('https://stefanbohacek.com/hellosalut/?lang=fr', data => {
    $('div#hello').text(data.hello);
  });
});
