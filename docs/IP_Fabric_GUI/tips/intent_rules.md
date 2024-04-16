---
description: In this section, we explain how to edit an intent verification rule or create a new one.
---

# Intent Verification Rules

## Edit Intent Verification Rule

Intent verification coloring rules can be fully customized. To do that, click
the **Pencil** icon next to a rule in the **Intent Verification Rules** box
above a technology table.

In our example, we will use the **Port-Channel Members State** rule above the
**Link Aggregation (LAG)/Portchannel/Etherchannel Member status table** (in
**Technology --> Port channels --> Member status table**).

![Port-Channel Members State intent rule](intent_rules/port-channel_members_state_intent_rule.png)

Now we can check and change the predefined coloring rules:

![Intent Rule Detail](intent_rules/intent_rule_detail.png)

Let's change the coloring from amber to red for `Aggregated interfaces with
membership status '(S)', '(F)', or '(I)'.`:

1. Remove rules from the amber color. Click the **amber color** and then the
   **Trash** icon next to each rule (the **Description** can be also removed):  
   ![Remove rules from color/state](intent_rules/remove_rules_from_color_state.png)
2. Click the **red color**.
3. Set the **Description** to `Aggregated interfaces with membership status
   '(S)', '(F)', or '(I)'.`
4. Use **+ Add rule** to add each of these rules regarding the `Member (Status)`
   column:
   - "`Members (Status)` contains `(s)`"
   - "`Members (Status)` contains `(f)`"
   - "`Members (Status)` contains `(i)`"
   - "`Members (Status)` contains `(d)`"
   - "`Members (Status)` contains `(DOWN)`"
5. Select logical `Or` because we want to mark a member red if any of the
   defined rules apply.
6. Click **Preview** to see if the rule works.
7. If it works as expected, click **Update**.
   ![Add rules in color/state](intent_rules/add_rules_in_color_state.png)

## Create Intent Verification Rule

You can also add a new set of coloring rules.

For example, if you want to check the aggregation protocol used in the **Link
Aggregation (LAG)/Portchannel/Etherchannel Member status table**:

1. Go to **Technology --> Port channels --> Member status table**.
2. Click `...` in the top-right corner of the table and select `Add intent
   verification rule`:  
   ![Add intent verification rule option](intent_rules/add_intent_verification_rule_option.png)
3. Specify the **Rule name**. For example, `Protocol Check`.
4. Select **Colorized column**. In our case, it's `Protocol`.
5. Leave **Dashboard Widgets** empty for now.
6. Click the **blue color**.
7. Create a rule "`Protocol` insensitive equal `lacp`".
   ![Create intent verification rule](intent_rules/create_intent_verification_rule.png)
8. Click the **amber color**.
9. Create a rule "`Protocol` equal `static`".
10. Click **Create**.  
    ![Create intent verification rule - remaining steps](intent_rules/create_intent_verification_rule_2.png)
