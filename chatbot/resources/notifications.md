1 answer

174 views

[Limit number of shown notifications](/forums/limit-number-of-shown-notifications "Limit number of shown notifications")

 If I have multiple incoming notifications, how do I limit the number that are visible ? Is there a property to set or is there a way I can programmatically remove certain toasts?

Thank you

  

[

Notification

](/forums/blazor?tagId=1046&searchText=notifications "Notification")

![](/forums/images/avatarimages/default.gif)

Svetoslav Dimitrov

Telerik team

![](/forums/images/forum-gamification/support-officer.svg)

 answered on 25 Nov 2022

1 answer

613 views

[Notification Only Works from Some Code](/forums/notification-only-works-from-some-code "Notification Only Works from Some Code")

This turned out to be a cache problem. Thought I cleared it, but apparently not. Today it works.  

I'm trying to implement some very basic toast notifications in a simple form WASM app.

There are two code paths where notifications would be displayed, based on form data. One of them works perfectly every time. The other refuses to work at all, despite the code being called.

I've tried all of the usual Visual Studio things (clean, deleting bin/obj, restarting, etc.) and the behavior persists. There's nothing in the browser's console to indicate a failure.  
This is my first attempt at using a Telerik control. It's also my first real Blazor app. Maybe there's something basic I didn't do correctly that's causing weird side effects. Nothing else really makes sense considering how simple this code is.

Here's the UI bits...  

<TelerikNotification @ref\="@NotificationReference" Class\="MyTelerikNotification" VerticalPosition\=NotificationVerticalPosition.Top HorizontalPosition\=NotificationHorizontalPosition.Center\></TelerikNotification\>
<h3\>@FlightTitle</h3\>
<ul\>
@foreach (var question in ThisFlightForm.Form.TrueFalseQuestions)
{
<FormQuestionTrueFalse thisFormItem\=question />
}
</ul\>
<div\>
<button @onclick\="OnClick\_BtnSubmit" class\="btn"\>Submit</button\>
<button @onclick\="OnClick\_BtnCancel" class\="btn"\>Cancel</button\>
</div\>

Inside the code block is the Notification Reference declaration:  

public TelerikNotification NotificationReference { get; set; } = new();

Here's the method call that's having issues. The obvious thing to check is the value of canSubmit, which works perfectly fine.  
If I put the ShowToasts calls from the IF down into the ELSE, they are fine.

private void OnClick\_BtnSubmit()
{
var canSubmit = \_preSubChecks.CanFormBeSubmitted(ThisFlightForm);
if (canSubmit.ChecksPassed)
{
//this does not work at all, despite being called
ShowToasts($"Unable to submit form - {canSubmit.ErrorMsg}", ThemeConstants.Notification.ThemeColor.Error);
ShowToasts("Submitting Form", ThemeConstants.Notification.ThemeColor.Info);
ShowToasts("Success!", ThemeConstants.Notification.ThemeColor.Success);
}
else
{   //this works fine
ShowToasts($"Unable to submit form - {canSubmit.ErrorMsg}", ThemeConstants.Notification.ThemeColor.Error);
}

}

Here's the method that shows the toast notifications. I added a temp var and a console out so I could verify the object wasn't null for some reason.  

private void ShowToasts(string msg, string toastType)
{
var tmpNm = new NotificationModel()
{
Text = msg,
ThemeColor = toastType,                
};
NotificationReference.Show(tmpNm);
Console.WriteLine(JsonConvert.SerializeObject(tmpNm));
}

Here's the output from the console logs where the Notification control refuses to display (the if):

{"ThemeColor":"error","Closable":true,"CloseAfter":5000,"ShowIcon":true,"Icon":null,"Text":"Unable to submit form - "}
{"ThemeColor":"info","Closable":true,"CloseAfter":5000,"ShowIcon":true,"Icon":null,"Text":"Submitting Form"}
{"ThemeColor":"success","Closable":true,"CloseAfter":5000,"ShowIcon":true,"Icon":null,"Text":"Success!"}

The first Notification (the error) is only here just to make sure the problem wasn't the content or the Notification display type being a problem.  

Here's the output from the one that works (the else):  

{"ThemeColor":"error","Closable":true,"CloseAfter":5000,"ShowIcon":true,"Icon":null,"Text":"Unable to submit form - At least one question was not answered"}

Aside from the Text, this is exactly the same as the error notification I put into the code that refuses to work.  

[

Notification

](/forums/blazor?tagId=1046&searchText=notifications "Notification")

![](/forums/images/avatarimages/default.gif)

[Adam](/forums/profile/6790df19-f658-436d-9df8-482513778b42)

Top achievements

![](/forums/images/forum-gamification/rank-01.svg) Rank 1

![](/forums/images/forum-gamification/blazor_ninja_level_1_icon.svg) Iron

 answered on 01 Jul 2022

0 answers

118 views

[Notifications breaking change](/forums/notifications-breaking-change "Notifications breaking change")

Hello,

After updating to 4.3.0 for Blazor, the close button on the notifications seem to be appearing at the bottom left.

![](/forums/embedded-images/1615865?index=0&c=67bf8361dcc447419c3dfc9166e3fec8)

Thanks,

Tony

[

Notification

](/forums/blazor?tagId=1046&searchText=notifications "Notification")

![](/forums/images/avatarimages/default.gif)

[Tony](/forums/profile/c265f961-e7e3-4f28-b25a-7194adbce14a)

Top achievements

![](/forums/images/forum-gamification/rank-01.svg) Rank 1

 asked on 12 Jul 2023

1 answer

354 views

[Notification click event with custom data](/forums/notification-click-event-with-custom-data "Notification click event with custom data")

I'm utilizing the notification and trying to implement a click event similar to this example:

[https://docs.telerik.com/blazor-ui/components/notification/templates#get-a-click-event-for-notification-body](https://docs.telerik.com/blazor-ui/components/notification/templates#get-a-click-event-for-notification-body)

My problem is that I need to get a custom field to my click event (i.e. the ID of a database record) that will be different for each notification. Is there anyway to pass custom data to the notification other than what is in the NotificationModel?

[

Notification

](/forums/blazor?tagId=1046&searchText=notifications "Notification")

![](/forums/images/adminimages/admin-user-292.jpg)

Dimo

Telerik team

![](/forums/images/forum-gamification/support-officer.svg)

 answered on 18 Nov 2021

1 answer

433 views

[How can you "clear all" notifications?](/forums/how-can-you-clear-all-notifications "How can you "clear all" notifications?")

I do not want to auto close my notifications and just let the user close them manually. But I would like to add a "clear all" button if they have not bothered to clear the notifications for some time. Seems like there should be an easy way to reset the collection but I have not found a way yet.

[

Accessibility

](/forums/blazor?tagId=13&searchText=notifications "Accessibility")[

Notification

](/forums/blazor?tagId=1046&searchText=notifications "Notification")[

Styling

](/forums/blazor?tagId=1441&searchText=notifications "Styling")

![](/forums/images/avatarimages/default.gif)

Marin Bratanov

Telerik team

![](/forums/images/forum-gamification/support-officer.svg)

 answered on 28 Apr 2021

1 answer

531 views

[Issue with Telerik Notification Component in Blazor Server: Notifications Not Rendering Across Threads](/forums/issue-with-telerik-notification-component-in-blazor-server-notifications-not-rendering-across-threads "Issue with Telerik Notification Component in Blazor Server: Notifications Not Rendering Across Threads")

I'm encountering an issue with the Telerik Notification component in my Blazor Server. The problem arises when I attempt to display a notification from a function that is not on the same thread as the component. In such cases, the notification item doesn't render in the UI.

To address this, I've made a modification to my component by replacing `StateHasChanged` with `InvokeAsync(StateHasChanged)` to ensure thread safety during invocation.

I'd like to seek input to determine whether this is a bug in the Telerik component or if there's a better approach to solving this issue. Any advice or suggestions would be greatly appreciated. Thank you!  

USE:::![](/forums/embedded-images/1623551?index=0&c=7dd021ec22964b3e8fba693ed4b5297a)  
  
  
BEFORE:::  
![](/forums/embedded-images/1623551?index=1&c=e0958b6163ad4e0ba32f13dcd6145e4e)  
  
  
  
AFTER FIX::::  
![](/forums/embedded-images/1623551?index=2&c=06e3b71c43f84401a2410f1b048603a3)

[

Notification

](/forums/blazor?tagId=1046&searchText=notifications "Notification")

![](/forums/images/adminimages/admin-user-1965.jpg)

Nadezhda Tacheva

Telerik team

![](/forums/images/forum-gamification/support-officer.svg)

 answered on 18 Sep 2023

1 answer

196 views

[How can I show notifications in the foreground for modal forms using the "OneNotificationPerApp" example in Github?](/forums/how-can-i-show-notifications-in-the-foreground-for-modal-forms-using-the-onenotificationperapp-example-in-github "How can I show notifications in the foreground for modal forms using the "OneNotificationPerApp" example in Github?")

Using the approach in the example code of "OneNotificationPerApp" works great for non-modal forms.   However, modal forms that use this approach do show the notfication but its in the background,  not easily visible.  Is there a way to change that?  I tried chaning the z order to a high number but that didn't work.  Any suggestions would be great.  Thanks in advance!

Let me know if you need to see the code and I can zip it up and attach it.

[https://github.com/telerik/blazor-ui/tree/master/notification/single-instance-per-app](https://github.com/telerik/blazor-ui/tree/master/notification/single-instance-per-app)

[

Notification

](/forums/blazor?tagId=1046&searchText=notifications "Notification")

![](/forums/images/adminimages/admin-user-292.jpg)

Dimo

Telerik team

![](/forums/images/forum-gamification/support-officer.svg)

 updated answer on 18 Mar 2024

0 answers

179 views

[Multiple Progress Bar updates](/forums/multiple-progress-bar-updates "Multiple Progress Bar updates")

Hello,

I have a scenario where I have a Telerik Notification with a Telerik progress bar embedded.  I am looking to update the progress bar of multiple instances of the notification independently based in separate threads.

Would this be possible?

Thanks,

Tony

[

Notification

](/forums/blazor?tagId=1046&searchText=notifications "Notification")[

ProgressBar

](/forums/blazor?tagId=1171&searchText=notifications "ProgressBar")

![](/forums/images/avatarimages/default.gif)

[Tony](/forums/profile/c265f961-e7e3-4f28-b25a-7194adbce14a)

Top achievements

![](/forums/images/forum-gamification/rank-01.svg) Rank 1

 asked on 21 Dec 2022

2 answers

907 views

[Notification as a service not a cascading parameter](/forums/notification-as-a-service-not-a-cascading-parameter "Notification as a service not a cascading parameter")

Is there an example where the TelerikNotification component is used more like a service, similar to the [MessageBox callback example](http://https//github.com/telerik/blazor-ui/tree/master/common/message-box/callback-event/Controls/MessageBox)?

I would like to be able to raise notifications from my view models and not have to either raise an event for the view to handle, or pass the TelerikNotification instance down to the view model.

thanks

\-marc

[

Notification

](/forums/blazor?tagId=1046&searchText=notifications "Notification")

![](/forums/images/adminimages/admin-user-2008.jpg)

Hristian Stefanov

Telerik team

![](/forums/images/forum-gamification/support-officer.svg)

 answered on 03 Sep 2021

1 answer

388 views

[Notification Area](/forums/notification-area "Notification Area")

I would be nice if the Notification component would just render in the location where it was put by default.  Very strange that it doesn't.

[

Notification

](/forums/blazor?tagId=1046&searchText=notifications "Notification")

![](/forums/images/adminimages/admin-user-1965.jpg)

Nadezhda Tacheva

Telerik team

![](/forums/images/forum-gamification/support-officer.svg)

 answered on 09 Dec 2020