# Limit download BGP routes

The full routing table, including full BGP, may contain fewer than 700K
records in 2020. Downloading and processing such a large amount of data
is time-consuming and may not provide any relevant information about the
internal IP addressing scheme.  
In cases where we expect to discover a router with a full BGP table, we
can limit the total number of BGP routes stored in the database.

You can find the threshold configuration in the ***Settings → Advanced →
Discovery tab***.

The lower limit available is currently 10000 BGP routes. The IP Fabric
will read the full routing table but will filter BGP routes per the
threshold before storing them in the database.

<img src="attachments/102203417/102629526.png" class="image-left" loading="lazy" data-image-src="attachments/102203417/102629526.png" data-height="139" data-width="524" data-unresolved-comment-count="0" data-linked-resource-id="102629526" data-linked-resource-version="1" data-linked-resource-type="attachment" data-linked-resource-default-alias="2018-08-27 10_46_00-Settings - IP Fabric network infrastructure controller - IPFabric.png" data-base-url="https://ipfabric.atlassian.net/wiki" data-linked-resource-content-type="image/png" data-linked-resource-container-id="102203417" data-linked-resource-container-version="6" data-media-id="7be21bde-7cd9-4c94-8616-6b6d44813f6b" data-media-type="file" />

<div class="pageSectionHeader">

## Attachments:

</div>

<div class="greybox" align="left">

<img src="images/icons/bullet_blue.gif" width="8" height="8" />
[2018-08-27 10_46_00-Settings - IP Fabric network infrastructure
controller - IPFabric.png](attachments/102203417/102629526.png)
(image/png)  

</div>
