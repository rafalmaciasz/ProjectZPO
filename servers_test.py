#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from collections import Counter

from servers import ListServer, Product, Client, MapServer, Server, TooManyProductsFoundError

server_types = (ListServer, MapServer)


class ProductTest(unittest.TestCase):
    def test_name_validity(self):
        with self.assertRaises(ValueError):
            Product('fh', 2)
        with self.assertRaises(ValueError):
            Product('64gs', 5)


class ServerTest(unittest.TestCase):

    def test_get_entries_returns_proper_entries(self):
        products = [Product('P12', 1), Product('PP234', 2), Product('PP235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual(Counter([products[2], products[1]]), Counter(entries))
   
    def test_get_entries_returns_proper_list1(self):
        products = [Product('P12', 1), Product('P234', 2), Product('P235', 1)]
        for server_type in server_types:
            server = server_type(products)
            entries = server.get_entries(2)
            self.assertEqual(Counter([]), Counter(entries))

    def test_max_returned_entries(self):
        products = [Product('PP234',2), Product('PP237',2),Product('PP238',1),Product('PP235',2),Product('PP239',1),Product('PP240',2)]
        for server_type in server_types:
            server = server_type(products)
            with self.assertRaises(TooManyProductsFoundError):
                server.get_entries(2)

class ClientTest(unittest.TestCase):
    def test_total_price_for_normal_execution(self):
        products = [Product('PP234', 2), Product('PP235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(5, client.get_total_price(2))
    
    
    def test_total_price_for_normal_execution1(self):
        products = [Product('PP234', 0), Product('PP235', 3)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(3, client.get_total_price(2))

    
    def test_total_price_for_normal_execution2(self):
        products = [Product('PP234',2), Product('PP237',2),Product('PP238',1),Product('PP235',2),Product('PP239',1),Product('PP240',2)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(None, client.get_total_price(2))
    
    
    def test_total_price_for_normal_execution3(self):
        products = [Product('PP234',2), Product('PP237',2),Product('PP238',1),Product('PP235',2)]
        for server_type in server_types:
            server = server_type(products)
            client = Client(server)
            self.assertEqual(None, client.get_total_price(3))

if __name__ == '__main__':
    unittest.main()