3 answers

126 views

[Custom image as map](/forums/custom-image-as-map "Custom image as map")

Hi Team,

is it possible to use a custom image inside the map control to place markers on?

Next to the world map, we would like to provide some detailed information for buildings and use the building layout to place markers inside rooms.

Thank you very much in advance!

Alex

[

Map

](/forums/blazor?tagId=1883&searchText=custom%20maps "Map")

![](/forums/images/adminimages/admin-user-1965.jpg)

Nadezhda Tacheva

Telerik team

![](/forums/images/forum-gamification/support-officer.svg)

 answered on 19 Jun 2024

1 answer

237 views

[More info on Maps and Layers](/forums/more-info-on-maps-and-layers "More info on Maps and Layers")

My requirements:

*   Ability for user to add shapes (rectangle, square, circle) or image to a map.
*   Ability for the user to move that shape around on a map (drag and drop).
*   Ability for the user to save all the placed shape geolocations.
*   Ability to read the saved shape geolocations and place them on the map.

I did a little research on your Map control and it does seem to support layers and a specific layer  [type](https://docs.telerik.com/blazor-ui/components/map/layers/shape) called "shape".  However, when I look at the code sample I don't see any way to define the shape (circle, rectangle, etc.) nor provide dimensions for the shape (L X W) nor have a bitmap/image as a shape?

I also didn't see any drag and drop support?

Could I get answers to these questions and/or point me to documentation that supports my requirements?

Cheers, Rob.

[

Map

](/forums/blazor?tagId=1883&searchText=custom%20maps "Map")

![](/forums/images/adminimages/admin-user-292.jpg)

Dimo

Telerik team

![](/forums/images/forum-gamification/support-officer.svg)

 answered on 13 Mar 2024

1 answer

139 views

[DropdownList popup behind top-layer](/forums/dropdownlist-popup-behind-top-layer "DropdownList popup behind top-layer")

We have a custom control where we host a Google Map.  
We created custom google map controls and placed it like google maps api requires.  
Everything works fine when the control is normally displayed as shown here:

![](/forums/embedded-images/1589892?index=0&c=2785f9b78f6249b984d9501c19b4af51)

but when the user put the map in fullscreen mode, our dropdownlist can't be opened because the animation-container isn't placed within the hierarchy of the element hosting the map, causing the dropdownlist popup to be behind the "top-layer" element of the page.

![](/forums/embedded-images/1589892?index=1&c=b12e9ab0c582457faf7470813252e19f)

Technically the problem is that when an element is set in fullscreen mode (but this happens even for HTML dialog elements and popup), the browser create a special layer where it places these elements (and their childrens).  

In the case of dropdownlist, you create k-animation-container telerik-blazor elements straight under the app div, this mean that any dropdownlist (and i suppose combobox items and every component that has a "popup") can't be shown into fullscreen elements or HTML dialogs.

Is it possible to explicitly set the dropdownlist animation container where I want? How can I fix this problem without recreate a dropdownlist component?

Thanks

[

DropDownList

](/forums/blazor?tagId=552&searchText=custom%20maps "DropDownList")

![](/forums/images/adminimages/admin-user-292.jpg)

Dimo

Telerik team

![](/forums/images/forum-gamification/support-officer.svg)

 answered on 09 Dec 2022

3 answers

2.1K+ views

[How to filter Grid on a column that is a list?](/forums/how-to-filter-grid-on-a-column-that-is-a-list "How to filter Grid on a column that is a list?")

I populate the Grid with ~5000 results from a database. The Grid does the paging, sorting, and filtering in memory, except it won't filter for this one column that is a List<string> CustomerNamesList. I'm attempting to use the FilterMenuTemplate -- I just need a textbox and a dropdown like "Contains" and "Does Not Contain" but I can't figure out how to filter the Grid.

<GridColumn Field\="@(nameof(CustomerNamesList))" Title\="Customers" Sortable\="false" Filterable\="true"\>
<FilterMenuTemplate\>
<label for\="NameMenuFilter"\>Customer Name:</label\>
<TelerikTextBox Id\="NameMenuFilter" ValueChanged\="@((value) => UpdateCustomerNameFilter(value))"\> 
</TelerikTextBox\>
</FilterMenuTemplate\>
<Template\>
@\* display - loop thru List of customer names \*@ 
</Template\>
</GridColumn\>

This code gets hit, but it's not doing anything...

public void UpdateCustomerNameFilter(string itemValue)
{
var filter1 = partyNamesFilterContext.FilterDescriptor.FilterDescriptors\[0\] as FilterDescriptor;
filter1.Value = itemValue;
filter1.Operator = FilterOperator.Contains;
}

  

When I click Filter, it gives me a blazor.server.js error  
Error: System.ArgumentException: Provided expression should have string type (Parameter 'stringExpression')

Update

Here's what I'm using as the datasource to make things clearer: IEnumerable<Companies>  
So what it appears to me is that the Grid doesn't know how to filter on a List of objects like this List<string>   
  

public class Companies
{  
  public int Id {get; set;}
public List<string\> CustomerNamesList {get; set;} = new List<string\>();  
  // Other fields
}

   

  

[

Grid

](/forums/blazor?tagId=755&searchText=custom%20maps "Grid")

![](/forums/images/adminimages/admin-user-292.jpg)

Dimo

Telerik team

![](/forums/images/forum-gamification/support-officer.svg)

 answered on 12 Sep 2023

11 answers

7.4K+ views

[Binding DropDownList Value to complex model](/forums/binding-dropdownlist-value-to-complex-model "Binding DropDownList Value to complex model")

I'm wondering how I can two-way bind a TelerikDropDown selection to a complex model object rather than a primitive type such as an Id field. I'm trying to add a TelerikDropDownList to a page where the user can select a user-friendly name of an object and have that selection's value bound to the object itself rather than a primitive data type. For example:

`<TelerikDropDownList Data=``"@DropDownItems"` `TextField=``"LabelField"` `ValueField=``"ValueField"` `@bind-Value=``"@SelectedItem"``/>`

`@code {`

    `public` `List<GenericDropDownModel<Item>> DropDownItems {` `get``;` `set``; }`

    `public` `IEnumerable<Item> AllItems {` `get``;` `set``; }`

    `public` `Item SelectedItem {` `get``;` `set``; }`

    `protected` `override` `Task OnInitializedAsync()`

    `{`

        `AllItems = await DataService.LoadItems();`

        `SelectedItem = AllItems.First();`

    `}`

    `private` `void` `SetDropDownItems()`

    `{`

        `List<GenericDropDownModel<Item>> dropDownItems =` `new` `List<GenericDropDownModel<Item>>();`

        `if` `(AllItems !=` `null``)`

        `{`              

            `foreach``(var item` `in` `AllItems)`

            `{`

                `GenericDropDownModel<Item> dropDownItem =` `new` `GenericDropDownModel<Item>()`

                `{`

                    `ValueField = item,`

                    `LabelField = item.Name`

                `};`

                `dropDownItems.Add(dropDownItem);`

            `}`

        `}`

        `DropDownItemsItems = dropDownItems;`

    `}`

    `public` `class` `GenericDropDownModel<T>`

    `{`

        `public` `string` `LabelField {` `get``;` `set``; }`

        `public` `T ValueField {` `get``;` `set``; }`      

    `}`

    `public` `class` `Item`

    `{`

        `public` `string` `Name {` `get``;` `set``; }`

        `public` `IModel Model {` `get``;` `set``; }`

        `public` `IEnumerable<IOtherModel> OtherModels {` `get``;` `set``; }`      

    `}`

    `public` `class` `Model`

    `{`

        `public` `int` `Id {` `get``;` `set``; }`

        `public` `string` `Name {` `get``;` `set``; }`

        `public string Info { get; set; }`

        `public` `IAnotherModel MoreDetails {` `get``;` `set``; }`

    `}`

`}`

`The drop-down is not allowing me to bind to non-primitive types nor specify a property of a property, i.e.:`

`<TelerikDropDownList Data=``"@AllItems"` `TextField=``"Name"` `ValueField=``"@Model.Info"` `@bind-Value=``"@SelectedInfo"``/>`

`   I get the following error with the first code snippet scenario:`

``System.InvalidOperationException: Telerik.Blazor.Components.TelerikDropDownList`2[GenericDropDownModel`1[Item],Item] does not support the type`` `'Item'``.`

   ``at Telerik.Blazor.Components.Common.TelerikSelectBase`2.TryParseValueFromString(String value, TValue& result, String& validationErrorMessage)``

   ``at Telerik.Blazor.Components.Common.TelerikSelectBase`2.set_CurrentValueAsString(String value)``

   ``at Telerik.Blazor.Components.TelerikDropDownList`2.SelectItem(ListDataItem item)``

   ``at Telerik.Blazor.Components.TelerikDropDownList`2.OnParametersSetAsync()``

   `at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion(Task task)`

   `at Microsoft.AspNetCore.Components.ComponentBase.RunInitAndSetParametersAsync()`

[

General Discussions

](/forums/blazor?tagId=709&searchText=custom%20maps "General Discussions")

![](/forums/images/avatarimages/default.gif)

[Víctor](/forums/profile/50c60d5c-d9a8-4d35-99ea-bf4b44eb8034)

Top achievements

![](/forums/images/forum-gamification/rank-01.svg) Rank 1

![](/forums/images/forum-gamification/general-questions-01.svg) Iron

![](/forums/images/forum-gamification/general-comments-01.svg) Iron

![](/forums/images/forum-gamification/blazor_ninja_level_1_icon.svg) Iron

 updated answer on 23 Aug 2023

1 answer

551 views

[TreeList - How can I determine if a row has the ability to expand/collapse?](/forums/treelist---how-can-i-determine-if-a-row-has-the-ability-to-expand-collapse "TreeList - How can I determine if a row has the ability to expand/collapse?")

Hi,

I've bound a TreeList to flat data. How can I determine if the TreeList has determined that a given row can be expanded/collapsed based upon the flat data, (i.e., how can I determine whether or not an expend/collapse arrow has been placed on the row)? This has an additional complexity in that the list cannot expand/collapse a row if it does not have children.

A use case for this would be to react to a double-click in a row and expand or collapse the row if the row is allowed to do that.

[

TreeList

](/forums/blazor?tagId=1612&searchText=custom%20maps "TreeList")

![](/forums/images/adminimages/admin-user-292.jpg)

Dimo

Telerik team

![](/forums/images/forum-gamification/support-officer.svg)

 answered on 15 Jun 2022

1 answer

238 views

[Gantt support for a minutes view coming in a future release?](/forums/gantt-support-for-a-minutes-view-coming-in-a-future-release "Gantt support for a minutes view coming in a future release?")

Great to see the new Gantt feature in update 2.26.  We immediately starting implementation for tracking our publishing stages at Microsoft for shipping software updates to show the parallelism of the processes and easily identify the relative time each stage takes.  This is a great improvement over a list in a table.   

Sadly, the current implementation of **Gantt only supports days** whilst our publishing stages take only a few minutes or hours.

I'm hoping additional **support for a minutes view** is coming soon as we had to shelve implementation of a Gantt view of publishing stages using your Gantt chart for the time being.  If it's not coming, an announcement of it's in the road map plan or not coming would be greatly appreciated by your marketing team.

[

Gantt

](/forums/blazor?tagId=1789&searchText=custom%20maps "Gantt")

![](/forums/images/adminimages/admin-user-1965.jpg)

Nadezhda Tacheva

Telerik team

![](/forums/images/forum-gamification/support-officer.svg)

 answered on 27 Sep 2021

2 answers

422 views

[Validation in ListView editing Problem](/forums/validation-in-listview-editing-problem "Validation in ListView editing Problem")

I am following the example for Validation in ListView Editing but I am having a problem.

The problem is that after I Save and Update to the ListView, it is calling CleanUpValidation but then is getting back into the code in EditTemplate and is therefore setting the currEditItem and currEditContext again to the Model that I just updated.

This is causing problems if I try to add a new item after the update it thinks the new item is valid when it isn't because the currEditContext's model still has the item I just updated.  

I can not figure out why it is getting back into the EditTemplate after Updating?

`<``EditTemplate``>`

    `@{`

        `currEditItem = context;`

        `if (currEditItem.Id == Guid.Empty)`

        `{`

            `currEditItem.Id = Guid.NewGuid();`

            `currEditItem.UserId = userId;`

            `currEditItem.FullName = GetUserName();`

            `currEditItem.DateWorked = DateTime.Today;`

            `currEditItem.TicketId = Ticket.Id;`

        `}`

        `if (currEditContext == null)`

        `{`

            `currEditContext = new EditContext(currEditItem);`

        `}`

        `<``EditForm` `EditContext``=``"@currEditContext"` `Context``=``"formContext"``>`

            `<``DataAnnotationsValidator` `/>`

            `<``ValidationSummary` `/>`

            `<``div` `class``=``"container-fluid editTimeEntry"``>`

                `<``div` `class``=``"row"``>`

                    `<``div` `class``=``"col"``>`

                        `<``ListViewCommandButton` `Command``=``"Save"` `Class``=``"float-right mr-1"` `Icon``=``"@IconName.Save"` `Title``=``"Save"``></``ListViewCommandButton``>`

                        `<``ListViewCommandButton` `Command``=``"Cancel"` `Class``=``"float-right"` `Icon``=``"@IconName.Cancel"` `Title``=``"Cancel"``></``ListViewCommandButton``>`

                    `</``div``>`

                `</``div``>`

                `<``div` `class``=``"row"``>`

                    `<``label` `for``=``"Staff"` `class``=``"font-weight-bold col-1"``>Staff</``label``>`

                    `<``div` `class``=``"col"``>`

                        `@if (isAdmin)`

                        `{`

                            `<``TelerikDropDownList` `@``bind-Value``=``"@currEditItem.UserId"` `Data``=``"@staff"` `Id``=``"Staff"`

                                                 `ValueField``=``"Id"` `TextField``=``"FullName"``>`

                            `</``TelerikDropDownList``>`

                        `}`

                        `else`

                        `{`

                            `<``span``>@currEditItem.FullName</``span``>`

                        `}`

                    `</``div``>`

                `</``div``>`

                `<``div` `class``=``"row"``>`

                    `<``label` `for``=``"DateWorked"` `class``=``"font-weight-bold col-1"``>Work Date</``label``>`

                    `<``div` `class``=``"col"``>`

                        `<``TelerikDatePicker` `Id``=``"DateWorked"` `@``bind-Value``=``"currEditItem.DateWorked"` `Format``=``"M/d/yyyy"` `Max``=``"DateTime.Today"``></``TelerikDatePicker``>`

                    `</``div``>`

                `</``div``>`

                `<``div` `class``=``"row"``>`

                    `<``label` `class``=``"font-weight-bold col-1"``>Time spent</``label``>`

                    `<``div` `class``=``"col-2"``>`

                        `<``label` `for``=``"TimeWorked"` `class``=``"mr-1"``>Time Worked</``label``>`

                        `<``span` `@``ref``=``"timeWorked"` `@onfocusin="(() => SelectOnFocus(timeWorked))">`

                            `<``TelerikNumericTextBox` `Id``=``"TimeWorked"` `Value``=``"@currEditItem.TimeWorked"`

                                                   `Format``=``"#0.00 hr"` `Decimals``=``"2"` `Step``=``".25"`

                                                   `ValueChanged="@( (double v) => TimeWorkedChangeHandler(v) )"`

                                                   `ValueExpression="@( () => currEditItem.TimeWorked )">`

                            `</``TelerikNumericTextBox``>`

                        `</``span``>`

                    `</``div``>`

                    `<``div` `class``=``"col-2"``>`

                        `<``label` `for``=``"BillabeTime"` `class``=``"mr-1"``>Billable Time</``label``>`

                        `<``span` `@``ref``=``"billableTime"` `@onfocusin="(() => SelectOnFocus(billableTime))">`

                            `<``TelerikNumericTextBox` `Id``=``"BillabeTime"` `Value``=``"@currEditItem.BillableTimeWorked"`

                                                   `Format``=``"#0.00 hr"` `Decimals``=``"2"` `Step``=``".25"`

                                                   `ValueChanged="@( (double v) => BillableTimeWorkedChangeHandler(v) )"`

                                                   `ValueExpression="@( () => currEditItem.BillableTimeWorked )">`

                            `</``TelerikNumericTextBox``>`

                        `</``span``>`

                    `</``div``>`

                    `<``div` `class``=``"col"``></``div``>`

                `</``div``>`

                `<``div` `class``=``"row"``>`

                    `<``label` `for``=``"Comments"` `class``=``"font-weight-bold col-1"``>Comments</``label``>`

                    `<``div` `class``=``"col"``>`

                        `<``InputTextArea` `@``bind-Value``=``"currEditItem.Comments"` `/>`

                    `</``div``>`

                `</``div``>`

            `</``div``>`

        `</``EditForm``>`

    `}`

`</``EditTemplate``>`

`private async Task UpdateTimeEntryHandler(ListViewCommandEventArgs args)`

`{`

    `var timeEntry = (TimeEntryViewModel)args.Item;`

    `if (!currEditContext.Validate())`

    `{`

        `args.IsCancelled = true;`

        `return;`

    `}`

    `var dbTimeEntry = mapper.Map<``TimeEntryViewModel``, TimeEntry>(timeEntry);`

    `var result = await ticketRepository.SaveTimeEntry(dbTimeEntry);`

    `if (result)`

    `{`

        `int index = Ticket.TimeEntries.FindIndex(te => te.Id == timeEntry.Id);`

        `if (index > -1)`

        `{`

            `Ticket.TimeEntries[index] = mapper.Map<``TimeEntry``, TimeEntryViewModel>(dbTimeEntry);`

        `}`

        `UpdateTotals();`

    `}`

    `CleanUpValidation();`

`}`

`private void CleanUpValidation()`

`{`

    `currEditContext = null;`

    `currEditItem = null;`

`}`

[

ListView

](/forums/blazor?tagId=891&searchText=custom%20maps "ListView")

![](/forums/images/avatarimages/89554278-0672-420b-bd77-a0a40fb4819fbob-web.jpg)

[Bob](/forums/profile/c5e7edb5-05f4-49dc-a01a-e8d54587eb6e)

Top achievements

![](/forums/images/forum-gamification/rank-01.svg) Rank 1

![](/forums/images/forum-gamification/general-questions-01.svg) Iron

![](/forums/images/forum-gamification/general-veteran.svg) Veteran

![](/forums/images/forum-gamification/blazor_ninja_level_1_icon.svg) Iron

 answered on 01 Oct 2020

2 answers

939 views

[Unable to build SASS after upgrade to kendo-theme-default 6.7.0 and Blazor UI 4.4.0](/forums/unable-to-build-sass-after-upgrade-to-kendo-theme-default-6-7-0-and-blazor-ui-4-4-0 "Unable to build SASS after upgrade to kendo-theme-default 6.7.0 and Blazor UI 4.4.0")

I am using Blazor UI and have upgraded to latest version 4.4.0 also upgraded the kendo-theme-default to version 6.7.0.

Using dart sass version 1.66.1 for the build.

Not using all your components so in my vendors folder I have this imports in \_index.sass.

It used to work but not after the upgrade.

@import "../../node\_modules/@progress/kendo-theme-default/scss/treeview";
@import "../../node\_modules/@progress/kendo-theme-default/scss/tabstrip";
@import "../../node\_modules/@progress/kendo-theme-default/scss/grid";
@import "../../node\_modules/@progress/kendo-theme-default/scss/button";
@import "../../node\_modules/@progress/kendo-theme-default/scss/common";
@import "../../node\_modules/@progress/kendo-theme-default/scss/checkbox";
@import "../../node\_modules/@progress/kendo-theme-default/scss/textbox";
@import "../../node\_modules/@progress/kendo-theme-default/scss/loader";

in package.json

"scripts": {
"sass": "npx sass --quiet-deps ./sass/app.scss ./wwwroot/css/app.css",
"sass:watch": "npx sass --watch --quiet-deps ./sass/app.scss ./wwwroot/css/app.css"
},

Output from build  
  

\> npx sass --quiet-deps ./sass/app.scss ./wwwroot/css/app.css

Error: Can't find stylesheet to import.
╷
1 │ @import "@progress/kendo-theme-core/scss/functions/index.import.scss";
│         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
╵
node\_modules\\@progress\\kendo-theme-default\\scss\\core\\functions\\index.import.scss 1:9  @import
node\_modules\\@progress\\kendo-theme-default\\scss\\\_variables.scss 1:9                   @import
node\_modules\\@progress\\kendo-theme-default\\scss\\core\\\_index.scss 4:9                  @import
node\_modules\\@progress\\kendo-theme-default\\scss\\treeview\\\_index.scss 1:9              @import
sass\\vendors\\\_index.scss 2:9                                                          @import
sass\\app.scss 7:9                                                                     root stylesheet

Have been wasting another hour (:  
  
have modified the @import path in the Telerik source files 

  

$wcag-min-contrast-ratio: 4.5 !default;

// Variables
@import "../\_variables.scss";

//@import "@progress/kendo-theme-core/scss/index.import.scss";
@import "../../../kendo-theme-core/scss/functions/index.import.scss";

// Expose
@include exports("kendo-core-styles") {
@include kendo-core--styles();
}

And then I get this new error. Should I stop using Dart SASS?  
  
  

2>EXEC: Warning  DEPRECATION: Using / for division outside of calc() is deprecated and will be removed in Dart Sass 2.0.0.

Recommendation: math.div($a, $b) or calc($a / $b)

More info and automated migrator: https://sass-lang.com/d/slash-div

ÔòÀ
66 Ôöé     @return ( $a / $b );
Ôöé               ^^^^^^^
ÔòÁ
node\_modules\\@progress\\kendo-theme-core\\scss\\functions\\\_math.import.scss 66:15  k-math-div()
node\_modules\\@progress\\kendo-theme-default\\scss\\\_variables.scss 285:21          @import
node\_modules\\@progress\\kendo-theme-default\\scss\\core\\\_index.scss 4:9            @import
node\_modules\\@progress\\kendo-theme-default\\scss\\treeview\\\_index.scss 1:9        @import
sass\\vendors\\\_index.scss 4:9                                                    @import
sass\\app.scss 7:9                                                               root stylesheet

2>EXEC: Error  : Undefined mixin.
ÔòÀ
10 Ôöé Ôöî @include exports("kendo-core-styles") {
11 Ôöé Ôöé     @include kendo-core--styles();
12 Ôöé Ôöö }
ÔòÁ
node\_modules\\@progress\\kendo-theme-default\\scss\\core\\\_index.scss 10:1     @import
node\_modules\\@progress\\kendo-theme-default\\scss\\treeview\\\_index.scss 1:9  @import
sass\\vendors\\\_index.scss 4:9                                              @import
sass\\app.scss 7:9                                                         root stylesheet
2>------- Finished building project: Zeus.Client. Succeeded: False. Errors: 1. Warnings: 1
Build completed in 00:00:02.138

  

[

Styling

](/forums/blazor?tagId=1441&searchText=custom%20maps "Styling")

![](/forums/images/avatarimages/default.gif)

Zhuliyan

Telerik team

![](/forums/images/forum-gamification/support-officer.svg)

 answered on 04 Sep 2023

1 answer

499 views

[Tooltip Flickering](/forums/tooltip-flickering "Tooltip Flickering")

I'm using the Blazor Tooltip inside Scheduler ItemTemplates.  The content of my Tooltips is defined inside a Template.

Intermittently, the tooltip is flickering very fast as the mouse hovers between Scheduler events. I've not observed any patterns to the flickering behavior, as it sometimes ceases entirely.

In the past, when using Javascript to render rich content in tooltips, I've added a delay, but that doesn't appear to be an option with this control.

Any recommendations or workarounds to address this behavior?

[

Scheduler

](/forums/blazor?tagId=1294&searchText=custom%20maps "Scheduler")[

Tooltip

](/forums/blazor?tagId=1591&searchText=custom%20maps "Tooltip")

![](/forums/images/adminimages/admin-user-2008.jpg)

Hristian Stefanov

Telerik team

![](/forums/images/forum-gamification/support-officer.svg)

 answered on 15 Aug 2023