content = document.querySelector("#content");
// Wether we are currently requesting more submissions
let currently_loading = false;
// Last page that was requested
let current_page = 0;
let user = document.querySelector('#user-username').innerHTML;
let reached_end = false;

function loadSubmissions(page)
{
    if(!reached_end) {
        let submissions = fetch('/user/nextpage?p='+current_page.toString()+'&u='+user.toString()).then(response=>response.text()).then(data=>
        {content.innerHTML += data; reached_end = data=="";});
        currently_loading = false;
    }
}
window.addEventListener("scroll", (event) => {
    // Load more submissions if user has scrolled to bottom and we are currently not already loading in new submissions
    if(window.scrollY+window.innerHeight > document.body.scrollHeight && !currently_loading) {
        currently_loading = true;
        loadSubmissions(current_page++);
    }
});

loadSubmissions()