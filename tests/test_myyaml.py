#
# Copyright (c) 2016, SUSE LLC
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# * Neither the name of ceph-auto-aws nor the names of its contributors may be
# used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
import handson.myyaml as myyaml
# import logging
import unittest

from handson.test_setup import SetUp


class TestMyYaml(SetUp, unittest.TestCase):

    def test_stanza_missing(self):
        self.reset_yaml()
        with self.assertRaises(AssertionError):
            myyaml.stanza_is_present('bogus_stanza')

    def test_stanza_assignment(self):
        # existing stanza
        self.reset_yaml()
        orig_val = myyaml.stanza('delegates')
        self.assertEqual(orig_val, 1)
        new_val = 90125
        myyaml.stanza('delegates', new_val)
        self.assertEqual(myyaml.stanza('delegates'), new_val)
        myyaml.stanza('delegates', orig_val)
        self.assertEqual(myyaml.stanza('delegates'), orig_val)
        # non-existing stanza
        self.reset_yaml()
        with self.assertRaises(AssertionError):
            myyaml.stanza('prd', {})
