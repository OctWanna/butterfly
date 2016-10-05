# Butterfly: A Plugin for CFD Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Butterfly.
#
# You should have received a copy of the GNU General Public License
# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Set parameters for snappyHexMeshDict.
Read more about snappyHexMeshDict here:
    https://openfoamwiki.net/images/f/f0/Final-AndrewJacksonSlidesOFW7.pdf


    Args:
        _bbox: A geometry that represents bounding box of the the domain.
            It should be slightly bigger than the domain itself.
        _cellSizeXYZ_: Size of cell in X, Y and Z directions in Rhino model units.
            You can use a point component to input values.
        _gradXYZ_: Grading value for X, Y and Z. Use gradXYZ component to generate
            grading for X, Y and Z directions.
    Returns:
        blockMeshDict: Butterfly blockMeshDict.
"""

ghenv.Component.Name = "Butterfly_blockMeshDict"
ghenv.Component.NickName = "blockMeshDict"
ghenv.Component.Message = 'VER 0.0.02\nSEP_30_2016'
ghenv.Component.Category = "Butterfly"
ghenv.Component.SubCategory = "03::Mesh"
ghenv.Component.AdditionalHelpFromDocStrings = "2"

try:
    # import butterfly
    from butterfly.gh.geometry import GHBFBlockGeometry
    from butterfly.gh.block import GHBlock
    from butterfly.gh.unitconversion import convertDocumentUnitsToMeters
    from butterfly.blockMeshDict import BlockMeshDict
    from butterfly.boundarycondition import BoundingBoxBoundaryCondition
except ImportError as e:
    msg = '\nFailed to import butterfly. Did you install butterfly on your machine?' + \
            '\nYou can download the installer file from github: ' + \
            'https://github.com/mostaphaRoudsari/Butterfly/tree/master/plugin/grasshopper/samplefiles' + \
            '\nOpen an issue on github if you think this is a bug:' + \
            ' https://github.com/mostaphaRoudsari/Butterfly/issues'
        
    raise ImportError('{}\n{}'.format(msg, e))

# create blockMeshDict based on BBox
if _bbox:
    block = GHBlock(_bbox, _cellSizeXYZ_, _gradXYZ_)
    print "Number of divisions: {}, {} and {}".format(*block.nDivXYZ)
    bc = BoundingBoxBoundaryCondition()
    BBBlockSurface = GHBFBlockGeometry('boundingbox', [_bbox.ToBrep()], bc)
    blockMeshDict = BlockMeshDict(convertDocumentUnitsToMeters(),
                                  [BBBlockSurface], [block])