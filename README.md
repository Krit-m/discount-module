## Requirement

- 'json' python library

## Instruction

- Use 'discountCalculator.py' as the main program. Functions for campaign check and discount calculations are created in
  the 'modules' folder.<br/><br/>
- The module receive input from the file 'shoppingList.json', which includes items in the shopping cart and discount
  campaigns chosen to be used. Items' categories are supposed to be specified in this list.<br/><br/> The terms used in
  json input and the module for discount categories and types are as following:<br/><br/>- Coupon : "coupon"<br/>- On
  Top : "onTop"
  <br/>- Seasonal: "seasonal"
  <br/><br/>- Fixed amount : "fixed"<br/>- Percentage discount : "percent"<br/>- Percentage discount by item
  category : "byItem"<br/>- Discount by points : "byPoints" <br/>- Special campaigns: "special" <br/><br/>The terms for
  parameters are as following:<br/><br/>- Amount, percentage, or Customer points: "amount" <br/>(for any campaigns with
  only one numerical parameter)<br/><br/>-Item category: "item"<br/>(for percentage discount by item
  category)<br/> <br/>- Every X THB: "forEvery"<br/>- Discount Y THB: "discount"<br/>(for special
  campaigns) <br/><br/> **In addition**, I've added the 'currentPromotion.json' file as another input. This adaptation
  aims to reflect the real life condition, in which some promotions might be usable only during a specific period of
  time. (Therefore, this input should only be edited by the store.) The file contains names (or code)
  referring to the promotional campaigns. Campaigns in 'shoppingList.json' with different names than the ones in this
  file are considered unusable.<br/><br/>
- Upon starting the program, the validity of each discount campaign is checked. A campaign in the list with any of the
  following properties is counted as 'Invalid':
    - Does not have a name, or its name is not included in 'currentPromotion'. For example, campaign 'HappyNewYear' is
      not used.
    - Discount category (coupon, on top, or seasonal) and type (i.e. fixed amount or percentage discount) are unmatched.
      For example; "category" : "coupon", "type" : "byItem"
    - Missing a required parameter or parameter value does not match. For example, string value for "amount".
    - "amount" is not a positive integer, or higher than 100 for percentage discounts.
    - "byItem" campaign, in cases that its specified item category does not match any items in the cart.
    - "special" campaign, with "discount" value higher than "forEvery"<br/><br/>
- The program does not stop working when encounter an invalid campaign. It will continue the discount calculation with
  any valid campaigns remain. The program will be interrupted and return a NOTICE message under 2 circumstances:
    - There are no valid campaigns left in the list.
    - There are 2 or more valid campaigns of a same category in the list.<br/><br/>
- Discount calculations are performed in order by category (coupon > on top > seasonal), regardless of campaigns' order
  in the list. (Even if you put an 'on top' before a 'coupon' in the list, 'coupon' will be used first.)<br/><br/>
- Names and types of campaigns used are shown in the terminal, along with the discounted total price.
    - For 'byItem', the item category is included in the output.
    - For 'byPoints', the amount of point used is stated in the output

## Other assumptions made

- For every discount campaigns in which the discount would be applied to the 'total price', the discount is applied in a
  certain percentage to EVERY ITEM in the cart, so that the total price is deducted to the desired amount. <br><br>This
  decision is to avoid conflicts in cases that a fixed amount discount, which is a coupon, is applied before '
  percentage discount by item category', an on top discount that might not be applied on all the items. This way, all
  items' price are reduced by 'fixed amount' equally before going through 'percentage discount by item category'.
  <br/><br/>
- If the 'fixed amount' coupon have higher amount than the total price, the total will be cut down to 0 baht, not a
  price of negative number. Also, other campaigns in the list are not used. However, if the shopping list include other
  2 or more campaigns of a same category, the list will not pass the validity step.<br/><br/>
- If point input for 'discount by points' is higher than 20 percent of the total price, following the point rule, the
  module will use only '20% of total price' points for discount. **(Please note that the amount of point actually being
  used is shown in the output.)**<br/> I assume that since this module only 'calculate' the discount, it will not
  consume customer's point without approval.