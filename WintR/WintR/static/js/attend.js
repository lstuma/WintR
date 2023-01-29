function attend(event)
{
    // Get caller from event
    let caller = event.target;
    let submission_id = caller.getAttribute('submission');
    // Update attending status and update counter of people attending
    fetch('/attend?s='+submission_id).then(response=>response.text()).then(data=>
    document.querySelector('#submission-attendee-count-'+submission_id).innerHTML=data+' attending');
    // Update button
    let attend_button = document.querySelector('#submission-attend-button-'+submission_id)
    if(attend_button.classList.contains('submission-button-not-attend'))
    {
        attend_button.classList.remove('submission-button-not-attend')
        attend_button.classList.add('submission-button-attend')
    }
    else
    {
        attend_button.classList.remove('submission-button-attend')
        attend_button.classList.add('submission-button-not-attend')
    }
}