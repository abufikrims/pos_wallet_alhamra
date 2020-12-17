# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name" : "POS Customer Wallet Alhamra",
    "version" : "12.0.0.6",
    "category" : "Point of Sale",
    "depends" : ['base','sale','account','point_of_sale'],
    "author": "BrowseInfo",
    'summary': 'This apps helps manage customer wallet and allow recharge wallet for the customer for ALHAMRA',
    "description": """
    
    Purpose :- 
This Module allow the seller to recharge wallet for the customer. point of sales wallet management , wallet in pos , wallet point of sale 
    POS Customer Wallet Management
    POS Wallet Management
    point of sale Wallet Management
    point of sales Wallet management
    Customer Wallet payment with POS
    Customer wallet POS
    customer credit POS
    POS customer credit payment    
    POS Customer Wallet payment Management
    POS Wallet payment Management
    point of sale Wallet payment Management
    point of sales Wallet payment management
    wallet on POS
    wallet on point of sale
        Wallet on website and POS, pay order using wallet balance
        eCommerce Wallet payment
        payment using wallet
        wallet balance.
        shop Wallet payment
        website wallet payment
        payment wallet
        payment on website using wallet
        wallet payment method
        Wallet on website and pay order using wallet balance
        eCommerce Wallet payment
        payment using wallet
        wallet balance.
        shop Wallet payment
        website wallet payment
        payment wallet
        payment on website using wallet
        Odoo wallet payment method
        Odoo website wallet add money on wallet management
        Odoo add money on pos wallet management
        Odoo recharge wallet for website and pos
        online store wallet management
        odoo webshop wallet management
        Odoo customer wallet management for website
        Odoo customer wallet management for POS
        odoo wallet recharge on pos
        Odoo wallet recharge on Website
        Website wallet customer management
        Add credit on Wallet

        POS Customer Wallet Management
        POS Wallet Management
        point of sale Wallet Management
        point of sales Wallet management
        Customer Wallet payment with POS
        Customer wallet POS
        customer credit POS
        POS customer credit payment    
        POS Customer Wallet payment Management
        POS Wallet payment Management
        point of sale Wallet payment Management
        point of sales Wallet payment management
        wallet on POs
        wallet on point of sale
This Module allow the seller to recharge wallet for the customer. 
    POS Customer Wallet Management
    POS Wallet Management
    point of sale Wallet Management
    point of sales Wallet management
    Customer Wallet payment with POS
    Customer wallet POS
    customer credit POS
    POS customer credit payment    
    POS Customer Wallet payment Management
    POS Wallet payment Management
    point of sale Wallet payment Management
    point of sales Wallet payment management
    wallet on POs
    wallet on point of sale
    This Odoo apps allow digital wallet/e-wallet facility in Odoo eCommerce/online store/webshop and POS. 
    This Odoo module is complete features of customer digital wallet management system which manages the wallet balance, 
    pay orders and bill using e-Wallet, recharge wallet. Single wallet use on point of sale as well as on Odoo Website/Webstore. 
    ccounting entries managed properly Whenever wallet amount use for payment or recharge done for wallet as well as when first time balance allocated on wallet. 
    This Odoo apps also have automatic email send features when wallet amount will be updated i.e Recharge or payment from wallet.
    If you want to manage customer wallet on Odoo then this will be the good Odoo app for use. 
    By using this app you can easily add/update wallet balance of your customer . 
    This wallet can be used as Payment on time of pos payment and eCommerce Order Payment with specific Journal. 
    Customer wallet balance can easily shown on each customer card and on POS screen as well as on Website Wallet section. 
    So don't need to go back and check each customer's wallet balance. 
    It has feature to pay partially or fully using Wallet and rest of the payment can also able to pay using other payment method(On Both POS and Website).
    Odoo website/ecommerce store digital wallet helps client engagement increased by build community of wallet user, 
    you can attract more customers by giving offer and discount on your wallet.
    This module allow digital wallet/e-wallet facility in Odoo eCommerce also on Point of Sale as Odoo e-Wallet it is must have feature for your Odoo.
    
    """,
    "website" : "https://www.browseinfo.in",
    "price": 55,
    "currency": "EUR",
    "data": ['security/ir.model.access.csv',
        'views/custom_pos_view.xml',
        'views/wallet.xml',
        'views/wallet_transaction.xml',
    ],
    'qweb': [
        'static/src/xml/pos.xml',
    ],
    "auto_install": False,
    "installable": True,
    'live_test_url':'https://youtu.be/G91ZKBTQL2Y',
    "images":['static/description/Banner.png'],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
