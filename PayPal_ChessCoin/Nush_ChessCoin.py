import hashlib
from ChessCoin.models import ChessCoin_Transaccions
from Authentication.models import User
from MultiplayerOnline.models import ChessLobbies
from django.db import IntegrityError
from decimal import Decimal
from django.utils import timezone
import pdb
class NushChessCoin:
    def __init__(self,hash=None, amount=None, payment_id=None, payer_id=None, merchant_id=None, ChessCoin_SKU=None, create_time=None, update_time=None):
        original_prices = {
            '2.41':2.00,
            '5.57':5.00,
            '10.84': 10.00,
            '26.65': 25.00,
            '53.00': 50.00,
            '106.90': 100.00
        }
        self.hash = hash
        self.amount = original_prices[amount] if amount != None else None
        self.payment_id = payment_id
        self.payer_id = payer_id
        self.merchant_id = merchant_id
        self.ChessCoin_SKU = ChessCoin_SKU
        self.create_time = create_time
        self.update_time = update_time
    
    def split_ChessCoin(self):

        id_number = ['5baa61e4c9b93f3f0682250b6cf8331b',   '6dcd4ce23d88e2ee9568ba546c007c63',   '9c56e3b214a65d9a1b69d92d0e7e5451',   '0cc1752700a0e7d627d0a1c6e6f5d3a9',   'a7c1f5c75a05b4f70d88586e0e0b2905',   '6dcd4ce23d88e2ee9568ba546c007c63',   'b6d767d2f8ed5d21a44c5e5f6e8c1429',   '3c59dc048e885024e846121d554c06c0',   '9d5ed678fe05708e8c8b73feffdc6d01',   'e99a18c428cb38d5f260853678922e03',   '22b8a735e8aee0746fa80d08c17f4f12',   '44bdde4646e60c80007b6a7268f58b03',   '5e3ef7d5823e9e0e56b93c4854b8d9e3',   'b3d08c1a3be95f9dd0185f0d132b8f6d',   '6e107f7bfb76a7b528a3e055b9e5d372',   '3d9b1d155a9fd02b3dfb70e5a0dc6a6c',   '4a564e9b3d3d4de437576c91cb1d3d79',   '7f2d3b81f5893448684a684b5a74f5d0',   '23e4e7f6dc95bb830790d184b29533bc',   '2bba8104478d40a3a63b4703a3e92d1d',   'ef3b84cf6d287fc28d04c8eaaf14a48c',   '3b6e3085f0483e4b5eb6862906eb8d63',   '7d8f6d2b706021d8f9d0d4586dcb8fc5',   '34fe647d60a5f71246215de6d0a7f6fc',   '3a3ea7d8a3ee8e74f8a2a4f0f3a4f118',   '8e11b0e51b9dfda2b9f2f5e77985c15f',   '5cf70c295d107c83663a601b2fcbff44',   '8ef0bfb78169161bca3ae90cf52735db',   '8d473734a832b7c82a3ea12d8b623aba',   'dc073a2e4a02a46051567d7808d5bfa5',   'ef45cdb53e80b325afc8546a6ad0f75f',   '2c63a7a6e7fc3b5ab846040787348ed6',   '8f9717ae3cb823d06c88e28e52909cf9',   '8d7a457f19a432bcf636d586f5dcd4ef',   '64d9b19d6a35ab2e5adf499fc5173e7b',   'c7c3f3b99f041bba21b75b10f47bbf3f',   'ba7329b23590f605a2dcd17fdcf53d1d',   '8bb0d3a0678abf8e5e14d67ae905e979',   'e960a16c3c5e50e8a62f4d8e7a61d4e2',   '7d6c0ab6f69de6f3e843a002044ab2e4',   'e81770998ea1c9b8c504c1fdb5b77c68',   'a8b735f77b726865cbfa6a251bd6a5c5',   '81045d6d93b7b5b4b482a5c2a02189a1',   'ab75d07b66569c5fa7983ecf42b8394c',   '4f70948924d7d2fdc6c48b5acfc06e95',   '3d23478e42a9d839d437ebf0f9c7857a',   '4b7b3dcb7285d78fbc58d6b34b12c2f6',   '6c4851f45901f6dbe69f60b90ff62dc1',   '3c8a693b0e686dd460282d1b0f6824fa',   '29cf19edc8e04ae8d387e546b0d5489f',   '8e0e62a3057d859d728436b3f8823dbb',   'd8d3c53c251f19e3b68a09ecad1d5e47',   '3d237892fb77d228ce9c69d70ac8eb85',   'b5d425b0ec1ab17d70cf39352e9fc4d4',   '8f8d435a1aafadf6782b8ab0f71b4176',   'd96d578e0055cc52ff77403c87d27c2e',   '9a6b65c6ef36b0f923b8ac9a673d4c7f',   '99a2c1c75c63b68a6b6704a70b281e3a',   '9d885f4f8de0c734730f77f4a99d9494',   'b87b070ee6043945b963bcbcd01a4e56',   'e0c6f4f2f5a8826d756682dce77f27c3',   '751b8d6f93a7d75f21b4b96b0c14ae4b',   'c8da302a19ed4eb2b8c674618a3b27ef',   '3c72a2856e626a4d46bcd28d63726f4f',   '72b4c89a6c8144c087f00f56c2088b20',   '6ccf22c3d27a2dd7753d1f64458302a6',   '6034609d3884d7a38c3ed7dcb4d239a2',   '8f9d0a1245fce86128e845a5b8934d3d',   'b1e1241a1f7d85d70d7167c7d47320d5',   '77b90a90c457a63b66c2482b0a2f02d7',   '741c40fa21e9b7ed5e8c2b5a1e76568c',   'd5b5dbac46a8631e8904acb7eec7150a',   'd83bbd7d69f78e26b2445725d318eb56',   '9b993bfc264c3cf2f38878e1db7c6b3e',   'ab0697360de39e1b12c1f59c0b2e9247',   'a13c6b69c64e592ded7d1d6607d8e92b',   'ba5809dff517dd3e0b82ae2a2f303b06',   '1b6b3fae1c1c742d7ae7d7c1a8b99bfa',   '0ec052b9f9a760d38c62e30cf9f0eae7',   '7c8b4f496b5a22795b2f44f7e107c579',   '3e2e5f824d002d9eb350fdddf5c28db4',   '73b873cb896f7b756f47b45e28c82ff8',   'e9b439b8db0d1a26b81cbf8262722e9a',   'b4c2f28f638f9d49b1b6f8b1542acb86',   '67de2d16a8fd77b0b5c6c7d1c468449d',   'f95f87e1cb094d703d064e3e0262dd04',   '5e527d53b7686d6fd1fc0fa208b95312',   'cbe9b4e5ac8a0916d30a05b379d2b7d1',   'b2cf5d1527e67a6fffe7c0c60360d1e6',   '57f3a94c31c0c5c5642db896b1bb8d57',   '42fc4318c2565a3ad74b2b04d31a18ba',   '4cfc8b7c437fd50c052a7e70c67f9797',   'aa2a9b220f36a048e4b41b6ae3350d0c',   '2b8fa5c66043ec2f12b095d61ae5b5b4',   'b6a36838a8a0c65b920a1b02dc527c80',   'a2d1a0c4d515052b2c97fd55957d5c91',   '0920a6f606e87154d47871d0f8b12d71',   'b0e5c64828eb2b26f8c1ac8ac2f1e064',   'e558f0cf9b61b7ebad3e383bfb05e52e',   '4e89f4c635b91aef54d5869b40e5060f',   'a02fc9c792a9e38fc8310a0c09b285b5',   'e541c5e0c84d4f1d2351343a03dc3a86',   '98df53b572f3b1b84b43e928df08c4f4',   'f5c67df41c6b09ab2b94b8efb0213a89',   '41ffb30d8e1bb490ed79046cf10a7551',   'b4c1dbf3b71c8bcb6a4d593d47de1f6c',   '6eaaed2ac8c5d36dff2fdc9a5d4b8106',   '4b6d7dc92659b8390cb6d2c963c25d74',   '7e5d0896b09187f22f55a43265c911e5',   '77d9d8ed91fd62f4a586779f185d5f3d',   '64452e02e7cb208b67c32b79f620e69d',   'b3e3b5b2681ac567dd5b4cf2e8fc4dbd',   'f5a339e3a556e95740c54c1844e7345f',   '5cf9d9a5b3b07f1d7f53760703a1f5fc',   'd12ec8d16b8cb539d8c75cc044334ee2',   'a6b3a1b84f63870b18a1c6f55659cfb6',   '86b3b23b7c8fa35d49f5e03f0e73dff6',   '45e2b7f17e77e76149e7118c712b462b',   '1e77c6e476d6a0e15c0e79de731f4b38',   '35d86fd1b8fd9b00ae55b1b6a4c92bfb',   'b1d4a7a6d382e6b0a0ed71c388bc7a12',   '5a7a9db7dbf682fe0b84384cfa0774fd',   '2d4d54d6ecb9a9b5a6de90d90397e8c4',   '87d4b7db3e0b6b19fc65a9b2a2e8e37e',   '8b0db45207de12e23872b378b4b88e9c',   '94de05e65d67ea16fa1d7b86dc8f4abf',   'fcb84f63c55b96eb1a09378a25f1f01b',   '7b70c18e46cbb5d3c6e4d7284f8d773f',   '7dcb48936d593c54ec917b9fa509e86e',   'a2cfa2d8d5f1161b94b79df93adbc107',   'f557b9e3c5c3f8ea2edb2351a6c17b5e',   '82b74b672a3e1d6f260bcb0c1341ed46',   '749b6055a27e423407a8f70dd3b79929',   '9c70acaf08892c26d6c3edc31d31774e',   'a17d9e1de5e96d8316a59e49644c9e3a',   '813cc848d3d505e68a4db3a44a885abe',   'd01a7ed59b800e9ac3b37ebd87787d54',   'b15284a94b0c15f92a204ee9d9a92b29',   '5826db9b1b63efc5eb4df9e86e2f9f85',   'ea2eb8b2071e03d434ef6c96e2f52742',   'e433045a9f5a37f64835a0654b80c663',   '43a9f48cf194ed4189c29dc7df08e05a',   'c4f27bde31d62c722a1dc1608d6f67b0d',   '9e0984dcdedbc9168dd5960a28c5d0b6',   'b8e42b76e9d09a98b5460d8d83d0ac84',   '44d8f7e0c474550dd4b0b75e4b5c91da',   '2bba3c014d582aa6f2cb620dff87cb54',   'e0a8df7c87b08e55fcff9b1e40d0acfe',   '378f4f6f0612e0b32e6c8b81d2b6bb70',   '42dbab8856b22087b54a7f83a6c44d35',   '6fc6f1b0c96f091b642f8b6c85df5ae2',   'a7d5d178d37958f41f39e782847ba39b',   'd5585493792b657fc391bc0890f8b55a',   'dcd457b63a4e84c674594dbe622b16f3',   '50db7d14c7399a25c04617f0ea0924fa',   'c2588738a62416e6eb80f3bcb57d4ac0',   '1ad68e8ec2c29caa3cf7d67e4f220f4b',   '058f49355f468c58fc865d76dbe02f8d',   '529c42c493c6851b080b2ef64463bfc8',   '6e8437fc94ea2e9fcf0398a25846c686',   '9b81c68a73e87b4a8cda6b9dba0944ff',   'fdb6b95328c16c42c64d1223d283b903',   '0b434a1b03607e15b8eabf37f1d839f5',   '91b5de89701493d14a2b3de68864558f',   '22f50b0e393f567a74206b78769e0096',   '38eeb03a16f6d5a3fa3c9a7c5aa1a4cb',   '76d4d29ac038d2b91676045ed62e29a5',   'f835872d27a4274a212d65cbd5427a52',   'c73d13dcdde81f40fba2b56b66a8a409',   'e7036d87358b88a3b8e87147d7b7378a',   '9ac23b4f9ea1a5e19e6d6b9b6482e9cc',   '63fc3d732dd07b9dbe87310f6d9c76a8',   '0a04204ad0a08c70d6034d2f7ae94585',   'd7f5e2ff68a5d6d3a703ae5a40e2f18f',   '5bdfc73d69c41c069cbb510e22b67189',   'f63fcf6f48ef4d3b5c906f5d3b973d38',   'c8fcb14f282b6a4c12d8ea0d43cf9b7d',   '02b6d8e1a627ef83540794d19cc724ba',   '7128b460d17b06c8a63447775fcd0a2b',   '5b38b5d5c87253e7dc46e279773eabf5',   'bd1c01fdad89ea78248994dbefc46a77',   '4fda51ec23590db8f1567ec2b6bb5d48',   'e85446f54c26740eb1d9443c8b3e478e',   '59e3fcdd47e7f7d25e594fbf7d27eb54',   'd79b29f5d788b2186897e5d896e7bb78',   'c37e9d042e852d5e9b089cb3c09a1c5a',   'e9f3c48d1d9e303b1bb8d2f59f1e7817',   '62b5f0b2e6b8dbf5d1e6e94b56a7343f',   'e8e5bcd91f8285f3d13c3a7069a7f3db',   '8e9ae8ecb9b2e3a0276f4c3d09f538d8',   '54c92db65eaf62f06e0925e8ebad7ef7',   'be053c7cf6c3888c67f0520d8a8f9b2e',   '7d7d1d1e6ad8b28d46e64b275569e43e',   '67a314d21c7072d68951a2671d56964d',   '7e6d1d16158fefb4d91fd82c5f6e6f59',   '87f6c6c2d122a61cb20979dcf56f0052',   '2f27e767575e69ae344c33f208d9ae90',   '8d9e388f9d94f9d90b547f58e04b3f0d',   'ec6dfb70b00c673ab3d626828b2b68f0',   'ae4d57fa7bdfb9f3640dbda394047f5a'  ]

        Nush_ChessCoin = []
        for i in range(int(float(self.amount)) * 2):
            data = f'{self.ChessCoin_SKU}-{self.merchant_id}-{self.amount}-{self.payment_id}-{self.hash}-{self.payer_id}-{self.create_time}-{self.update_time}-{id_number[i]}'
            Nush_ChessCoin.append(hashlib.sha256(data.encode('utf-8')).hexdigest())
        
        return {self.ChessCoin_SKU:Nush_ChessCoin}


    
    def create_transaction(self, id):
        lobby = ChessLobbies.objects.filter(id=id).first()
        white_player = User.objects.get(username=lobby.white_player)
        black_player = User.objects.get(username=lobby.black_player) 
        amount = lobby.amount
        if white_player.wallet >= amount and black_player.wallet >= amount:
                white_player.wallet -= amount
                black_player.wallet -= amount
                
            
                white_player.save()
                black_player.save()
                lobby.save()
                creating_transaction = ChessCoin_Transaccions.objects.create(
                    id=lobby.id,
                    white_player=lobby.white_player,
                    black_player=lobby.black_player,
                    game_status=lobby.game_status,
                    timer_black_player=lobby.timer_black_player,
                    timer_white_player=lobby.timer_white_player,
                    timer=lobby.timer,
                    amount=lobby.amount ,
                    lobby_wallet=amount*2,
                    fee_match_amount= (lobby.amount / 2) if lobby.amount < Decimal(9.99) else (lobby.amount * Decimal(0.10)),
                    validation_message='CCNR'
                )
                return True
        else:
            return False

        
    def complete_transaccion(self, id):
        try:
            lobby = ChessLobbies.objects.get(id=id)
            transaction_info = ChessCoin_Transaccions.objects.get(id=id)
            if transaction_info.validation_message == 'CFT50' or transaction_info.validation_message == 'CFT10':
                return True
        except ObjectDoesNotExist:
            return

        if lobby.game_status in ['Check Mate!', 'draw']:
            transaction_info.this_chessboard = lobby.this_chessboard
            transaction_info.winning_player = lobby.winning_player
            transaction_info.ended_at = timezone.now()
            transaction_info.transaccion_status = True
            
            if lobby.winning_player in [lobby.white_player, lobby.black_player]:
                winning_player = User.objects.get(username=lobby.winning_player)

                if lobby.amount < Decimal('9.99'):
                    reward = lobby.amount + (lobby.amount / 2)
                    transaction_info.validation_message = 'CFT50'
                else:
                    reward = lobby.amount + (lobby.amount * Decimal('0.90'))
                    transaction_info.validation_message = 'CFT10'

                winning_player.wallet += reward
                winning_player.save()
                
            transaction_info.save()




    def cancel_transaction(self, id):
        lobby = ChessLobbies.objects.filter(id=id).first()
        white_player = User.objects.get(username=lobby.white_player)
        black_player = User.objects.get(username=lobby.black_player) 
        transaction_info = ChessCoin_Transaccions.objects.filter(id=id).first()

        amount = lobby.amount / Decimal(2)

        white_player.wallet += amount
        black_player.wallet += amount
        transaccion_info.validation_message = 'CCRR'
        transaccion_info.game_status = 'Cancelled [CCRR]'
        white_player.save()
        black_player.save()
        transaccion_info.save()
        return True

