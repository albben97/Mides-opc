import logging
import asyncio
import sys
sys.path.insert(0, "..")

from asyncua import ua, Server, Node
from asyncua.common.methods import uamethod



@uamethod
def func(parent, value):
    return value * 2


async def main():
    _logger = logging.getLogger('asyncua')
    # setup our server
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://127.0.0.1:4840")

    # setup our own namespace, not really necessary but should as spec
    uri = 'http://examples.freeopcua.github.io'
    idx = await server.register_namespace(uri)

    # populating our address space
    # server.nodes, contains links to very common nodes like objects and root
    noder1 = await server.nodes.objects.add_variable("s=GVL.R1","GVL.R1", False, varianttype=ua.VariantType.Boolean)
    noder2 = await server.nodes.objects.add_variable("s=GVL.R2","GVL.R2", False, varianttype=ua.VariantType.Boolean)
    noder3 = await server.nodes.objects.add_variable("s=GVL.R3","GVL.R3", False, varianttype=ua.VariantType.Boolean)
    noder4 = await server.nodes.objects.add_variable("s=GVL.R4","GVL.R4", False, varianttype=ua.VariantType.Boolean)
    noder5 = await server.nodes.objects.add_variable("s=GVL.R5","GVL.R5", False, varianttype=ua.VariantType.Boolean)
    noder6 = await server.nodes.objects.add_variable("s=GVL.R6","GVL.R6", False, varianttype=ua.VariantType.Boolean)
    noder7 = await server.nodes.objects.add_variable("s=GVL.R7","GVL.R7", False, varianttype=ua.VariantType.Boolean)
    nodes1 = await server.nodes.objects.add_variable("s=GVL.S1","GVL.S1", False, varianttype=ua.VariantType.Boolean)
    nodes2 = await server.nodes.objects.add_variable("s=GVL.S2","GVL.S2", False, varianttype=ua.VariantType.Boolean)
    nodes3 = await server.nodes.objects.add_variable("s=GVL.S3","GVL.S3", False, varianttype=ua.VariantType.Boolean)
    nodes4 = await server.nodes.objects.add_variable("s=GVL.S4","GVL.S4", False, varianttype=ua.VariantType.Boolean)
    nodes5 = await server.nodes.objects.add_variable("s=GVL.S5","GVL.S5", False, varianttype=ua.VariantType.Boolean)
    nodes6 = await server.nodes.objects.add_variable("s=GVL.S6","GVL.S6", False, varianttype=ua.VariantType.Boolean)
    nodes7 = await server.nodes.objects.add_variable("s=GVL.S7","GVL.S7", False, varianttype=ua.VariantType.Boolean)
    nodes8 = await server.nodes.objects.add_variable("s=GVL.S8","GVL.S8", False, varianttype=ua.VariantType.Boolean)
    node_reset = await server.nodes.objects.add_variable("s=GVL.RESET","GVL.RESET", False, varianttype=ua.VariantType.Boolean)


    await noder1.set_writable()
    await noder2.set_writable()
    await noder3.set_writable()
    await noder4.set_writable()
    await noder5.set_writable()
    await noder6.set_writable()
    await noder7.set_writable()
    await nodes1.set_writable()
    await nodes2.set_writable()
    await nodes3.set_writable()
    await nodes4.set_writable()
    await nodes5.set_writable()
    await nodes6.set_writable()
    await nodes7.set_writable()
    await nodes8.set_writable()
    await node_reset.set_writable()

    # noder1 = Node(idx,"s=GVL.R1")
    # noder2 = Node(idx,"s=GVL.R2")
    # noder3 = Node(idx,"s=GVL.R3")
    # noder4 = Node(idx,"s=GVL.R4")
    # noder5 = Node(idx,"s=GVL.R5")
    # noder6 = Node(idx,"s=GVL.R6")
    # noder7 = Node(idx,"s=GVL.R7")
    # nodes1 = Node(idx,"s=GVL.S1")
    # nodes2 = Node(idx,"s=GVL.S2")
    # nodes3 = Node(idx,"s=GVL.S3")
    # nodes4 = Node(idx,"s=GVL.S4")
    # nodes5 = Node(idx,"s=GVL.S5")
    # nodes6 = Node(idx,"s=GVL.S6")
    # nodes7 = Node(idx,"s=GVL.S7")
    # nodes8 = Node(idx,"s=GVL.S8")
    # node_reset = Node(idx,"s=GVL.RESET")


    # Set MyVariable to be writable by clients
    
    #await server.nodes.objects.add_method(ua.NodeId('ServerMethod', 2), ua.QualifiedName('ServerMethod', 2), func, [ua.VariantType.Int64], [ua.VariantType.Int64])
    _logger.info('Starting server!')
    _logger.info('Starting server!')
    _logger.info('Starting server!')
    async with server:
        while True:
            await asyncio.sleep(1)
            #new_val = await myvar.get_value() + 0.1
            #_logger.info('Set value of %s to %.1f', myvar, new_val)
            #await myvar.write_value(new_val)


if __name__ == '__main__':

    #logging.basicConfig(level=logging.DEBUG)

    asyncio.run(main(), debug=True)
